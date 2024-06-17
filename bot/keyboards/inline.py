from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from db.models import Wallet, Currency

from .callback import (WalletCallbackData, WalletActionCallbackData, WalletActions,
                       BackButtonCallbackData, BackButtonActions)
from .buttons import WalletActionsButtons, InlineButtons


def build_back_query_factory(callback: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(text=InlineButtons.BACK.value,
                                callback_data=BackButtonCallbackData(a=callback).pack())


def wallet_list_factory(wallets: List[Wallet]) -> InlineKeyboardMarkup:
    """
    Generates wallet list keyboard
    """
    _keyboard = [
        [InlineKeyboardButton(text=f"{wallet.id} ({wallet.currency.code})",
                              callback_data=WalletCallbackData(id=wallet.id).pack())]
        for wallet in wallets
    ]

    _keyboard.append(
        [InlineKeyboardButton(text=InlineButtons.NEW_WALLET.value,
                              callback_data=WalletActionCallbackData(a=WalletActions.NEW_WALLET).pack())]
    )

    _keyboard.append(
        [InlineKeyboardButton(text=InlineButtons.ALL_WALLETS.value,
                              callback_data=WalletActionCallbackData(a=WalletActions.ALL_WALLETS).pack())]
    )

    return InlineKeyboardMarkup(inline_keyboard=_keyboard)


def wallet_actions_factory(wallet: Wallet) -> InlineKeyboardMarkup:
    """
    Generates wallet actions keyboard
    """
    _keyboard = [
        [InlineKeyboardButton(text=button,
                              callback_data=WalletActionCallbackData(id=wallet.id, a=action).pack())]
        for button, action in zip(WalletActionsButtons, WalletActions)
    ]

    _keyboard.append(
        [build_back_query_factory(BackButtonActions.RENDER_MAIN_MENU.value)]
    )

    return InlineKeyboardMarkup(inline_keyboard=_keyboard)


def currencies_list_factory(currencies: List[Currency]) -> InlineKeyboardMarkup:
    """
    Generates currencies list keyboard
    """
    _keyboard = [
        [InlineKeyboardButton(text=f"{currency.code} ({currency.rate} USDT)",
                              callback_data=WalletActionCallbackData(id=currency.id, a=WalletActions.CONFIRM_CUR).pack())]
        for currency in currencies
    ]

    _keyboard.append(
        [build_back_query_factory(BackButtonActions.RENDER_MAIN_MENU.value)]
    )

    return InlineKeyboardMarkup(inline_keyboard=_keyboard)
