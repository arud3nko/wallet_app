from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import F
from aiogram.filters import Command, CommandStart, MagicData

from . import core
from ..filters import Authorized
from ..states import AuthStates
from ..keyboards import buttons, reply
from ..template_engine import render_template

from db.models import User

if TYPE_CHECKING:
    from aiogram import Dispatcher, types


AuthFilter = MagicData(F.user.authorized)


async def start(message: types.Message, user: User):
    """
    Handles /start command
    """
    if user.authorized:
        return await message.reply(
            text=render_template(
                name="already_authorized.html"
            ),
            reply_markup=None
        )

    await message.reply(
        text=render_template(
            "greeting.html",
            button=buttons.ReplyButtons.Start
        ),
        reply_markup=reply.start_keyboard_factory()
    )


def setup(dp: Dispatcher) -> Dispatcher:
    """
    Sets up core handlers

    :param dp: `Dispatcher` instance
    """
    dp.message.register(start, CommandStart())
    dp.message.register(core.start_auth, F.text == buttons.ReplyButtons.Start)
    dp.message.register(core.handle_passcode, AuthStates.entering_passcode)
    dp.message.register(core.logout_user, Command("logout"), Authorized)

    return dp
