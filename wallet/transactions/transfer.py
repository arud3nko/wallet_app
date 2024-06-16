from __future__ import annotations

from ..types.transaction import Transaction
from ..core.wallet import Wallet
from ..exceptions.transactions import IncompatibleCurrencies, NotEnoughBalance


class Transfer(Transaction):
    """Transfer balance transaction"""
    def __init__(self,
                 src: Wallet,
                 dest: Wallet,
                 amount: float):
        """
        Transfer balance transaction

        :param src: Source wallet
        :param dest: Destination wallet
        :param amount: Transaction amount
        """
        super().__init__(src, dest, amount)
        if src.currency != dest.currency:  # Checking for incompatible currencies
            raise IncompatibleCurrencies(transaction=self)

    def execute(self) -> None:
        """Subtracts source balance with transaction amount & Summaries destination balance with same amount"""
        amount = super().amount

        if super().src.balance < amount:  # Checking for not enough balance
            raise NotEnoughBalance(transaction=self)

        super().src.balance -= amount
        super().dest.balance += amount
