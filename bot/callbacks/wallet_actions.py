from aiogram import types, Dispatcher, F
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User
from db.service import wallet, currency

from .. import states

from ..handlers.core import render_wallet
from ..keyboards import inline
from ..keyboards.callback import WalletCallbackData, WalletActionCallbackData, WalletActions, BackButtonActions
from ..template_engine import render_template


async def show_wallet_actions(
        query: types.CallbackQuery,
        db_session: AsyncSession,
        callback_data: WalletCallbackData):
    """
    Handles wallet actions callback
    """

    _wallet_id = callback_data.id

    _wallet = await wallet.get_wallet_by_id(db_session, _wallet_id)

    text, markup = await render_wallet(_wallet)

    await query.message.edit_text(
        text=text,
        reply_markup=markup
    )

    await query.answer()


async def top_up_balance(
        query: types.CallbackQuery,
        db_session: AsyncSession,
        callback_data: WalletActionCallbackData,
        state: FSMContext):
    """Handles TopUp action"""

    _wallet_id = callback_data.id

    _wallet = await wallet.get_wallet_by_id(db_session, _wallet_id)

    await state.set_state(states.TopUpBalance.entering_amount)
    await state.update_data(wallet_id=_wallet_id)

    await query.message.delete()
    await query.bot.send_message(
        chat_id=query.from_user.id,
        text=render_template("top_up_amount.html",
                             wallet=_wallet)
    )

    await query.answer()


async def new_wallet(
        query: types.CallbackQuery,
        db_session: AsyncSession):
    """Handles New Wallet action"""

    _currencies = await currency.get_all_currencies(db_session)

    await query.message.edit_text(
        text=render_template("new_wallet.html"),
        reply_markup=inline.currencies_list_factory(_currencies)
    )

    await query.answer()


async def new_wallet_currency_confirmed(
        query: types.CallbackQuery,
        db_session: AsyncSession,
        user: User,
        callback_data: WalletActionCallbackData):
    """Creates new wallet"""
    _wallet = await wallet.create_wallet(db_session, user.id, int(callback_data.id))
    await query.message.delete()
    await query.bot.send_message(
        chat_id=query.from_user.id,
        text=render_template("new_wallet_created.html")
    )

    text, markup = await render_wallet(_wallet)

    await query.message.answer(
        text=text,
        reply_markup=markup
    )

    await query.answer()


async def all_wallets(
        query: types.CallbackQuery,
        db_session: AsyncSession):
    """Handles all wallets list request"""

    _wallets = await wallet.get_all_wallets(db_session)

    await query.message.edit_text(
        text=render_template("all_wallets.html",
                             wallets=_wallets),
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[[inline.build_back_query_factory(BackButtonActions.RENDER_MAIN_MENU.value)]]
        )
    )

    await query.answer()


def setup(dp: Dispatcher) -> Dispatcher:
    dp.callback_query.register(show_wallet_actions, WalletCallbackData.filter())
    dp.callback_query.register(top_up_balance, WalletActionCallbackData
                               .filter(F.a == WalletActions.TOP_UP))
    dp.callback_query.register(new_wallet, WalletActionCallbackData
                               .filter(F.a == WalletActions.NEW_WALLET))
    dp.callback_query.register(new_wallet_currency_confirmed, WalletActionCallbackData
                               .filter(F.a == WalletActions.CONFIRM_CUR))
    dp.callback_query.register(all_wallets, WalletActionCallbackData
                               .filter(F.a == WalletActions.ALL_WALLETS))
    return dp
