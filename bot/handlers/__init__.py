from __future__ import annotations

from typing import TYPE_CHECKING

from .commands import setup as setup_commands
from .transactions import setup as setup_transactions

if TYPE_CHECKING:
    from aiogram import Dispatcher


def setup(dp: Dispatcher) -> Dispatcher:
    setup_commands(dp)
    setup_transactions(dp)

    return dp
