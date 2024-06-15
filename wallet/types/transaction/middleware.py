from __future__ import annotations

from abc import ABC, abstractmethod

from typing import Callable

from .base import Transaction


class TransactionMiddleware(ABC):
    @abstractmethod
    def __call__(self, transaction: Transaction, call_next: Callable):
        pass
