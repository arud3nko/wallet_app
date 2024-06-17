from aiogram import Dispatcher

from .wallet_actions import setup as setup_wallet_actions
from .navigation import setup as setup_navigation


def setup(dp: Dispatcher) -> Dispatcher:
    setup_wallet_actions(dp)
    setup_navigation(dp)
    return dp
