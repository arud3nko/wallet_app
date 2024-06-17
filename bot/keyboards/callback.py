from typing import Optional, Union

from aiogram.filters.callback_data import CallbackData

from enum import Enum


class BackButtonActions(Enum):
    """Enum class"""
    RENDER_MAIN_MENU: str = "rmm"


class BackButtonCallbackData(CallbackData, prefix="b"):
    """Callback data for sending backwards action"""
    a: BackButtonActions


class WalletActions(Enum):
    """Enum class"""
    TOP_UP:         str = "top_up"
    TRANSFER:       str = "transfer"
    SHOW_WALLETS:   str = "show"
    NEW_WALLET:     str = "new"
    CONFIRM_CUR:    str = "conf_cur"
    ALL_WALLETS:    str = "aw"


class WalletCallbackData(CallbackData, prefix="w"):
    """Callback data for sending wallet id"""
    id: Union[int, str]


class WalletActionCallbackData(CallbackData, prefix="wa"):
    """Callback data for sending wallet action"""
    id: Optional[str | int] = None
    a: WalletActions
