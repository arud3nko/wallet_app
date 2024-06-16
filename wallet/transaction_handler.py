# transaction_handler.py

from __future__ import annotations

from typing import Optional, List, Literal

from .types.transaction import Transaction, TransactionMiddleware


class TransactionHandler:
    """TransactionHandler handles transactions"""
    def __init__(self):
        """Initializing"""
        self._pre_middlewares: List[TransactionMiddleware] = []
        """Pre-handler middlewares"""
        self._post_middlewares: List[TransactionMiddleware] = []
        """Post-handler middlewares"""

    @property
    def pre_middlewares(self) -> Optional[List[TransactionMiddleware]]:
        """Pre-handler middlewares property"""
        return self._pre_middlewares

    @property
    def post_middlewares(self) -> Optional[List[TransactionMiddleware]]:
        """Post-handler middlewares property"""
        return self._post_middlewares

    def add_pre_middleware(self, middleware: TransactionMiddleware):
        """Adds pre-handler middleware"""
        self._pre_middlewares.append(middleware)

    def add_post_middleware(self, middleware: TransactionMiddleware):
        """Adds post-handler middleware"""
        self._post_middlewares.append(middleware)

    def handle(self, transaction: Transaction):
        """Handles transaction: runs pre-handler middlewares -> transaction -> post-handler middlewares"""
        self._run_middlewares("pre_", transaction, 0, self._pre_middlewares)
        self._run_middlewares("post_", transaction, 0, self._post_middlewares)

    def _run_middlewares(self,
                         type_: Literal["pre_", "post_"],
                         transaction: Transaction,
                         index: int,
                         middlewares: List[TransactionMiddleware]):
        """Runs middleware chain. If no pre-handler middlewares provided, runs default handler"""
        if index < len(middlewares):
            middleware = middlewares[index]
            return middleware(transaction=transaction,
                              call_next=lambda: self._run_middlewares(
                                  type_=type_,
                                  transaction=transaction,
                                  index=index + 1,
                                  middlewares=middlewares))
        elif type_ != "post_":
            return transaction.execute()
        else:
            return
