from __future__ import annotations

from typing import Optional, List, Literal

from .types.transaction import Transaction, TransactionMiddleware


class TransactionHandler:
    def __init__(self):
        self._pre_middlewares: List[TransactionMiddleware] = []
        self._post_middlewares: List[TransactionMiddleware] = []

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
        self._run_middlewares("pre_", transaction, 0, self._pre_middlewares)
        self._run_middlewares("post_", transaction, 0, self._post_middlewares)

    def _run_middlewares(self,
                         type_: Literal["pre_", "post_"],
                         transaction: Transaction,
                         index: int,
                         middlewares: List[TransactionMiddleware]):
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
