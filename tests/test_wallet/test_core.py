# pytest

import pytest

from wallet.core import Wallet, Currency


class TestWalletCore:
    """Core tests"""
    @pytest.fixture()
    def currency(self) -> Currency:
        return Currency("RUB", 100)

    def test_wallet_core(self, currency: Currency) -> None:
        wallet = Wallet(currency)

        assert wallet.balance == 0.0
        assert wallet.currency == currency.code
        assert isinstance(wallet.id, str)
