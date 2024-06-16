# wallet_handler.py
# aka Facade

from __future__ import annotations

from typing import Optional, List

from .core import Wallet, Currency
from .types.transaction import Transaction
from .transaction_handler import TransactionHandler


class WalletHandler:
    """WalletHandler class is a class that handles wallets and transactions"""
    def __init__(self,
                 wallets:       Optional[List[Wallet]] = None):
        """
        Initializing wallet handler

        :param wallets: List of Wallet instances
        """
        self.transaction_handler:   TransactionHandler = TransactionHandler()
        """Handles transactions in this Wallet handler"""
        self.wallets:               List[Wallet] = wallets if wallets else []

    def new_wallet(self, currency: Currency) -> Wallet:
        """
        Adds new wallet to this handler

        :param currency: New wallet's currency
        :return: Wallet instance
        """
        _wallet = Wallet(currency=currency)
        self.wallets.append(_wallet)
        return _wallet

    def provide(self, transaction: Transaction) -> None:
        """
        Provides transaction (sends it to the transaction handler)

        :param transaction: Transaction instance
        """
        self.transaction_handler.handle(transaction=transaction)
