# wallet_handler.py
# aka Facade

from __future__ import annotations

from .types.transaction import Transaction
from .transaction_handler import TransactionHandler
from .exceptions import TransactionException


class WalletHandler:
    """WalletHandler class is a class that handles wallets and transactions"""
    def __init__(self):
        """
        Initializing wallet handler

        """
        self.transaction_handler:   TransactionHandler = TransactionHandler()
        """Handles transactions in this Wallet handler"""

    def provide(self, transaction: Transaction) -> None:
        """
        Provides transaction (sends it to the transaction handler)

        :param transaction: Transaction instance
        """
        try:
            self.transaction_handler.handle(transaction=transaction)
        except TransactionException:
            raise
