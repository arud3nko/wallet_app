from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.ext.asyncio import AsyncSession

from db.service import user


class UserMiddleware(BaseMiddleware):
    """
    Middleware for providing a `User` object
    """

    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        await self._provide_user(data["event_from_user"].id, data)
        await handler(event, data)

    @staticmethod
    async def _provide_user(user_id: int, data: dict) -> dict:
        """
        Fetches and returns user
        """

        if 'db_session' not in data:
            raise RuntimeError("AsyncSession not found.")

        db_session: AsyncSession = data.get("db_session")

        u = await user.get_user_by_tg_id(db_session, user_id)

        if u is None:
            u = await user.create_user(db_session, tg_id=user_id)

        data["user"] = u

        return data
