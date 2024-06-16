from __future__ import annotations

from typing import TYPE_CHECKING

from uuid import uuid4

if TYPE_CHECKING:
    from ..core.currency import Currency


class Wallet:
    """Base wallet class"""
    def __init__(self, currency: Currency):
        self._id:           str = uuid4().__str__()
        self._currency:     Currency = currency
        self._balance:      float = 0.0

    @property
    def id(self) -> str:
        """Returns unique wallet identifier"""
        return self._id

    @property
    def balance(self) -> float:
        """Returns wallet balance"""
        return self._balance

    @property
    def currency(self) -> str:
        """Returns wallet currency code"""
        return self._currency.code

    @balance.setter
    def balance(self, val: float) -> None:
        self._balance = val
