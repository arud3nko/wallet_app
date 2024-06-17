from typing import TYPE_CHECKING, Tuple

import pytest

if TYPE_CHECKING:
    from wallet.types.transaction import Transaction

from wallet.core import Wallet, Currency
from wallet.transactions import TopUpBalance, Transfer


class TestTransactions:
    @pytest.fixture()
    def wallets_pair(self) -> Tuple[Wallet, Wallet]:
        rub = Currency(code="RUB", rate=95)
        src, dest = Wallet(user_id=1, id="1", currency=rub), Wallet(user_id=1, id="1", currency=rub)
        src.balance += 1000
        return src, dest

    def test_top_up_balance(self, wallets_pair: Tuple[Wallet, Wallet]):
        src, dest = wallets_pair

        amount = 1000
        src_balance = src.balance

        top_up: Transaction = TopUpBalance(src, amount)
        top_up.execute()

        assert src.balance == src_balance + amount

    def test_transfer(self, wallets_pair: Tuple[Wallet, Wallet]):
        src, dest = wallets_pair

        amount = 1000
        src_balance = src.balance
        dest_balance = dest.balance

        transfer: Transaction = Transfer(src, dest, amount)
        transfer.execute()

        assert src.balance == src_balance - amount
        assert dest.balance == dest_balance + amount
