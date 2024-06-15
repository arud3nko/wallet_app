from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Currency:
    code: str
    rate: float
