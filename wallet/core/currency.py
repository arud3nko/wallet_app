from __future__ import annotations

from pydantic import BaseModel


class Currency(BaseModel):
    """Currency dataclass"""
    code: str
    rate: float
