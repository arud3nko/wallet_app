import pytest

from wallet import WalletHandler
from wallet.core import Wallet, Currency

from wallet.transactions import Transfer

from wallet.exceptions import IncompatibleCurrencies, NotEnoughBalance, TransactionException


class TestWalletExceptions:
    @pytest.fixture()
    def currency(self) -> Currency:
        return Currency("RUB", 100)

    @pytest.fixture()
    def empty_wallet(self, currency: Currency) -> Wallet:
        return Wallet(currency=currency)

    @pytest.fixture()
    def not_empty_wallet(self, currency: Currency) -> Wallet:
        _ = Wallet(currency=currency)
        _.balance += 1000
        return _

    @pytest.fixture()
    def eur_wallet(self, currency=Currency("EUR", 100)):
        return Wallet(currency=currency)

    @pytest.fixture()
    def handler(self) -> WalletHandler:
        return WalletHandler()

    def test_not_enough_balance_exception(self,
                                          handler: WalletHandler,
                                          empty_wallet: Wallet,
                                          not_empty_wallet: Wallet):
        with pytest.raises(NotEnoughBalance) as exc_info:
            _ = Transfer(empty_wallet, not_empty_wallet, 1000)
            handler.provide(_)

        assert exc_info.errisinstance(TransactionException)

    def test_incompatible_currencies_exception(self,
                                               handler: WalletHandler,
                                               eur_wallet: Wallet,
                                               not_empty_wallet: Wallet):
        with pytest.raises(IncompatibleCurrencies) as exc_info:
            _ = Transfer(not_empty_wallet, eur_wallet, 1000)
            handler.provide(_)

        assert exc_info.errisinstance(TransactionException)
