from typing import Callable, Type, Tuple

import pytest

from wallet.core import Wallet, Currency

from wallet.transaction_handler import TransactionHandler
from wallet.types.transaction import TransactionMiddleware, Transaction


class CounterTransactionMiddleware(TransactionMiddleware):
    counter: int = 0

    def __call__(self, transaction: Transaction, call_next: Callable):
        CounterTransactionMiddleware.counter += 1
        return call_next()


class EmptyTransaction(Transaction):
    execution_counter: int = 0

    def execute(self) -> None:
        self.execution_counter += 1


class TestTransactionHandler:
    @pytest.fixture()
    def middleware(self) -> Type[TransactionMiddleware]:
        return CounterTransactionMiddleware

    @pytest.fixture()
    def wallets_pair(self) -> Tuple[Wallet, Wallet]:
        rub = Currency("RUB", 95)
        src, dest = Wallet(rub), Wallet(rub)
        src.balance += 1000
        return src, dest

    @pytest.fixture()
    def transaction(self, wallets_pair: Tuple[Wallet, Wallet]) -> Transaction:
        src, dest = wallets_pair
        return EmptyTransaction(src, dest, 10)

    def test_transaction_handler_middlewares(self,
                                             middleware: Type[TransactionMiddleware],
                                             transaction: Transaction):
        middleware.counter = 0
        transaction.execution_counter = 0

        handler = TransactionHandler()
        handler.add_pre_middleware(middleware())
        handler.add_post_middleware(middleware())

        handler.handle(transaction)

        assert middleware.counter == 2
        assert transaction.execution_counter == 1
