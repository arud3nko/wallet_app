from __future__ import annotations

from typing import TYPE_CHECKING, Union

from aiogram.fsm.context import FSMContext

from ..keyboards import buttons, reply, inline
from ..template_engine import render_template
from ..states import AuthStates

if TYPE_CHECKING:
    from aiogram import types

from db.models import User, Wallet


async def render_main_menu(
        user: User):
    """Sends main menu message (wallets list)"""

    text = render_template("welcome.html", user=user)
    markup = inline.wallet_list_factory(user.wallets)
    return text, markup


async def render_wallet(
        wallet: Wallet):
    """Renders single wallet"""

    text = render_template("wallet.html", wallet=wallet)
    markup = inline.wallet_actions_factory(wallet)
    return text, markup


async def start_auth(
        update: Union[types.CallbackQuery, types.Message],
        state: FSMContext,
        user: User):
    """Starting user authorization"""

    await state.set_state(AuthStates.entering_passcode)

    if user.passcode:
        return await update.bot.send_message(
            chat_id=update.from_user.id,
            text=render_template(
                "login.html"
            ),
            reply_markup=None
        )

    await update.bot.send_message(
        chat_id=update.from_user.id,
        text=render_template(
            "registration.html",
            button=buttons.ReplyButtons.Start
        ),
        reply_markup=None
    )


async def handle_passcode(
        update: Union[types.CallbackQuery, types.Message],
        user: User,
        state: FSMContext):
    """Save user passcode & checks it if needed"""

    _passcode: str = update.text

    if user.passcode:
        if user.passcode != _passcode:
            return await update.bot.send_message(
                chat_id=update.from_user.id,
                text=render_template(
                    "login_failed.html"
                ),
                reply_markup=None
            )
    else:
        user.passcode = _passcode

        await update.bot.send_message(
            chat_id=update.from_user.id,
            text=render_template(
                "registration_completed.html",
                user=user
            )
        )

    user.authorized = True
    await state.clear()

    text, markup = await render_main_menu(user)

    return await update.bot.send_message(
        chat_id=update.from_user.id,
        text=text,
        reply_markup=markup)


async def logout_user(
        update: Union[types.CallbackQuery, types.Message],
        user: User,
        state: FSMContext):
    """Logout user"""

    user.authorized = False

    await update.bot.send_message(
        chat_id=update.from_user.id,
        text=render_template(
            "logout.html",
            user=user
        ),
        reply_markup=reply.start_keyboard_factory()
    )

    await state.clear()
