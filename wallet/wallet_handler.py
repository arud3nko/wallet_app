from __future__ import annotations

from typing import Optional, List

from .core import Wallet
from .types import Transaction, Currency, TransactionHandler


class WalletHandler:
    def __init__(self,
                 transaction_handler: TransactionHandler,
                 wallets:       Optional[List[Wallet]] = None,
                 transactions:  Optional[List[Transaction]] = None):
        self.transaction_handler:   TransactionHandler = transaction_handler
        self.wallets:               List[Wallet] = wallets if wallets else []
        self.transactions:          List[Transaction] = transactions if transactions else []


