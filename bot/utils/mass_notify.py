from typing import List

from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest

from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User
from db.service import user


async def notify_all_users(bot: Bot,
                           session: AsyncSession,
                           text: str):
    """This function uses bot's method to notify all users from DB"""

    _users: List[User] = await user.get_all_users(session)

    for _user in _users:
        try:
            await bot.send_message(
                chat_id=_user.tg_id,
                text=text
            )
        except TelegramBadRequest:
            pass
