from typing import Callable

from wallet.types.transaction import TransactionMiddleware, Transaction


class LoggingPostMiddleware(TransactionMiddleware):
    """
    Simple middleware for testing. It handles every transaction and prints log about
    this transaction.
    """

    def __call__(self, transaction: Transaction, call_next: Callable):
        print(transaction)
        call_next()
