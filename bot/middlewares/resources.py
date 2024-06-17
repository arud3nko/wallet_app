from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from sqlalchemy.ext.asyncio import AsyncSession

from db.engine import engine

from wallet.wallet_handler import WalletHandler


class ResourcesMiddleware(BaseMiddleware):
    def __init__(self, wallet_handler: WalletHandler):
        self.wallet_handler = wallet_handler
        """Wallet handler"""
        super().__init__()

    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        resources = await self._provide_resources()
        data.update(resources)
        await handler(event, data)
        await self._cleanup(data)

    @staticmethod
    async def _provide_db_session() -> AsyncSession:
        """
        Provides `AsyncSession` object
        :return: Initialized session
        """

        session = AsyncSession(engine)

        return session

    def _provide_wallet_handler(self) -> WalletHandler:
        """
        Provides `WalletHandler` object
        """
        return self.wallet_handler

    async def _provide_resources(self) -> dict:
        """
        Initializes & provides resources
        :return:
        """
        db_session = await self._provide_db_session()
        wallet_handler = self._provide_wallet_handler()

        resources = {
            "db_session": db_session,
            "wallet_handler": wallet_handler
        }

        return resources

    @staticmethod
    async def _cleanup(data: dict):
        if "db_session" in data:
            session: AsyncSession = data["db_session"]
            await session.commit()
            await session.close()
