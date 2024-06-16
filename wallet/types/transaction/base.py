from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from abc import ABC, abstractmethod

from uuid import uuid4

if TYPE_CHECKING:
    from ...core.wallet import Wallet


class Transaction(ABC):
    """Base transaction class"""
    def __init__(self,
                 src: Optional[Wallet],
                 dest: Wallet,
                 amount: float):
        """
        Initialization

        :param src: Source wallet. For some reason, can be None :)
        :param dest: Destination wallet.
        :param amount: Transaction amount
        """
        self._id = uuid4().__str__()
        """Unique transaction identifier"""
        self._src = src
        self._dest = dest
        self._amount = amount

    def __repr__(self):
        """Transaction's string representation"""
        return (f"<{self.__class__.__name__}-"
                f"{self._id}_"
                f"from_{self._src.id if self._src else None}_"
                f"to_{self._dest.id}_"
                f"amount_{self._amount}>")

    @abstractmethod
    def execute(self) -> None:
        """Abstract execute method"""
        pass

    @property
    def id(self) -> str:
        """Returns transaction's unique identifier"""
        return self._id

    @property
    def dest(self) -> Optional[Wallet]:
        """Returns transaction's destination wallet"""
        return self._dest

    @property
    def src(self) -> Wallet:
        """Returns transaction's source wallet"""
        return self._src

    @property
    def amount(self) -> float:
        """Returns transaction's amount"""
        return self._amount
