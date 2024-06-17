from fastapi import APIRouter

from aiogram import Bot

from sqlalchemy.ext.asyncio import AsyncSession

from bot.utils.mass_notify import notify_all_users

from db.engine import Session

from .routes import BotAPIRoutes


class BotAPIRouter(APIRouter):
    """Simple router instance"""
    bot: Bot
    session: AsyncSession = Session()


router = BotAPIRouter()


@router.get(BotAPIRoutes.MASS_NOTIFY)
async def mass_notify(message:  str):
    """Notify all users. Provide message required"""
    await notify_all_users(bot=router.bot,
                           session=router.session,
                           text=message)
