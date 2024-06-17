from __future__ import annotations

from aiogram import types, Dispatcher
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from .. import states
from ..handlers.core import render_wallet
from ..template_engine import render_template

from db.service import wallet

from wallet.transactions import TopUpBalance
from wallet.wallet_handler import WalletHandler
from wallet.exceptions import TransactionException


async def top_up_balance(
        message: types.Message,
        wallet_handler: WalletHandler,
        db_session: AsyncSession,
        state: FSMContext):
    """Sends main menu message (wallets list)"""

    _amount = message.text

    if not _amount.isdigit():
        return await message.reply(
            text=render_template("provide_numeric.html")
        )

    data = await state.get_data()

    _wallet_id = data.get("wallet_id")
    _wallet = await wallet.get_wallet_by_id(db_session, _wallet_id)

    _transaction = TopUpBalance(dest=_wallet, amount=int(_amount))

    try:
        wallet_handler.provide(_transaction)
    except TransactionException as te:
        return await message.reply(
            text=str(te)
        )

    await state.clear()

    await message.reply(
        text=render_template("top_up_success.html", wallet=_wallet)
    )

    text, markup = await render_wallet(_wallet)

    return await message.answer(
        text=text,
        reply_markup=markup
    )


async def transfer():
    raise NotImplementedError


def setup(dp: Dispatcher) -> Dispatcher:
    dp.message.register(top_up_balance, states.TopUpBalance.entering_amount)
    return dp
