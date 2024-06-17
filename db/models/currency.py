from typing import TYPE_CHECKING, List

from sqlalchemy import Float, Column
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import Base, pk

if TYPE_CHECKING:
    from .wallet import Wallet


class Currency(Base):
    """This table stores currencies data"""
    __tablename__ = "currencies"

    id:         Mapped[pk]
    code:       Mapped[str]
    rate:       Column = Column(Float)

    wallets:    Mapped[List["Wallet"]] = relationship(back_populates="currency", lazy="selectin")
