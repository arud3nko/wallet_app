from __future__ import annotations

from typing import Hashable

from uuid import uuid4

from pydantic import BaseModel

from ..core.currency import Currency


class Wallet(BaseModel):
    """Base wallet class"""
    user_id:      Hashable
    id:           str = uuid4().__str__()
    currency:     Currency
    balance:      float = 0.0
