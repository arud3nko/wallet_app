from __future__ import annotations

from typing import Optional, List

from .core import Wallet, Currency
from .types.transaction import Transaction
from .transaction_handler import TransactionHandler


class WalletHandler:
    def __init__(self,
                 wallets:       Optional[List[Wallet]] = None):
        self.transaction_handler:   TransactionHandler = TransactionHandler()
        self.wallets:               List[Wallet] = wallets if wallets else []

    def new_wallet(self, currency: Currency) -> Wallet:
        _wallet = Wallet(currency=currency)
        self.wallets.append(_wallet)
        return _wallet

    def do(self, transaction: Transaction):
        self.transaction_handler.handle(transaction=transaction)
