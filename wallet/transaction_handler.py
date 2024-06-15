from __future__ import annotations

from typing import Optional, List, Callable

from .types.transaction import Transaction, TransactionMiddleware


class TransactionHandler:
    def __init__(self):
        self._pre_middlewares:   Optional[List[TransactionMiddleware]] = None
        self._post_middlewares:  Optional[List[TransactionMiddleware]] = None

    @property
    def pre_middlewares(self) -> Optional[List[TransactionMiddleware]]:
        return self._pre_middlewares

    @property
    def post_middlewares(self) -> Optional[List[TransactionMiddleware]]:
        return self._post_middlewares

    def add_pre_middleware(self, middleware: TransactionMiddleware):
        self._pre_middlewares.append(middleware)

    def add_post_middleware(self, middleware: TransactionMiddleware):
        self._post_middlewares.append(middleware)

    def handle(self, transaction: Transaction):
        pass

    def _run_middlewares(self, transaction: Transaction, index: int, middlewares: List[TransactionMiddleware]):
        if index < len(middlewares):
            middleware = middlewares[index]
            return middleware(transaction=transaction,
                              call_next=lambda: self._run_middlewares(
                                  transaction=transaction,
                                  index=index+1,
                                  middlewares=middlewares))
        else:
            return transaction.execute()