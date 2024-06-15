from __future__ import annotations

from uuid import uuid4

from wallet.types.currency import Currency


class Wallet:
    """Base wallet class"""
    def __init__(self, currency: Currency):
        self._id:           str = uuid4().__str__()
        self._currency:     Currency = currency
        self._balance:      float = 0.0

    @property
    def id(self) -> str:
        return self._id

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, val: float) -> None:
        self._balance = val
