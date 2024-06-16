from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Currency:
    """Currency dataclass"""
    code: str
    rate: float
