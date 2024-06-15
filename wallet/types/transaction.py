from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from uuid import uuid4

from .wallet import Wallet


class Transaction(ABC):
    """Base transaction class"""
    def __init__(self,
                 src: Optional[Wallet],
                 dest: Wallet,
                 amount: float):
        self._id = uuid4().__str__()
        self._src = src
        self._dest = dest
        self._amount = amount

    def __repr__(self):
        return (f"<{self.__class__.__name__}-"
                f"{self._id}_"
                f"from_{self._src.id if self._src else None}_"
                f"to_{self._dest.id}_"
                f"amount_{self._amount}>")

    @abstractmethod
    def execute(self) -> None:
        pass

    @property
    def id(self) -> str:
        return self._id

    @property
    def dest(self) -> Optional[Wallet]:
        return self._dest

    @property
    def src(self) -> Wallet:
        return self._src

    @property
    def amount(self) -> float:
        return self._amount
