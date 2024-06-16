from __future__ import annotations

from abc import ABC, abstractmethod

from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from .base import Transaction


class TransactionMiddleware(ABC):
    """Base middleware class"""
    @abstractmethod
    def __call__(self, transaction: Transaction, call_next: Callable):
        """Abstract __call__ method"""
        pass
