from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .currency import Currency
    from .user import User


class Wallet(Base):
    """This table stores wallets data"""
    __tablename__ = "wallets"

    id:             Mapped[str] = mapped_column(primary_key=True)
    balance:        Mapped[float]
    currency_id:    Mapped[int] = mapped_column(ForeignKey("currencies.id"))
    user_id:        Mapped[int] = mapped_column(ForeignKey("users.id"))

    currency:       Mapped["Currency"] = relationship(back_populates="wallets", lazy="selectin")
    user:           Mapped["User"] = relationship(back_populates="wallets", lazy="selectin")
