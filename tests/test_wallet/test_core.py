import pytest

from wallet.core import Wallet, Currency


class TestWalletCore:
    """Core tests"""
    @pytest.fixture()
    def currency(self) -> Currency:
        return Currency(code="RUB", rate=100)

    def test_wallet_core(self, currency: Currency) -> None:
        wallet = Wallet(user_id=1, id="1", currency=currency)

        assert wallet.balance == 0.0
        assert wallet.currency == currency
        assert isinstance(wallet.id, str)
