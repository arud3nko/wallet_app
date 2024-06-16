from __future__ import annotations

from typing import TYPE_CHECKING

from ..types.transaction import Transaction

if TYPE_CHECKING:
    from ..core.wallet import Wallet


class TopUpBalance(Transaction):
    """
    Top up balance transaction
    Sends None as a source wallet
    """
    def __init__(self,
                 dest: Wallet,
                 amount: float):
        """
        Top up balance transaction

        :param dest: Destination wallet
        :param amount: Top up amount
        """
        super().__init__(None, dest, amount)

    def execute(self) -> None:
        """Summaries destination wallet balance with transaction amount"""
        super().dest.balance += super().amount
