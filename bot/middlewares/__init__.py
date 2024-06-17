from __future__ import annotations

from typing import TYPE_CHECKING

from .resources import ResourcesMiddleware
from .user import UserMiddleware

if TYPE_CHECKING:
    from aiogram import Dispatcher
    from wallet.wallet_handler import WalletHandler


def setup(dp: Dispatcher, wallet_handler: WalletHandler) -> Dispatcher:
    """
    Sets up middlewares
    """
    dp.update.middleware(ResourcesMiddleware(wallet_handler))
    dp.update.middleware(UserMiddleware())

    return dp
