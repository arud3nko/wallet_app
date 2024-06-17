from typing import TYPE_CHECKING, List, Optional

from sqlalchemy.orm import Mapped, relationship

from .base import Base, pk

if TYPE_CHECKING:
    from .wallet import Wallet


class User(Base):
    """This table stores users data"""
    __tablename__ = "users"

    id:             Mapped[pk]
    tg_id:          Mapped[int]
    passcode:       Mapped[Optional[str]]
    authorized:     Mapped[Optional[bool]]

    wallets: Mapped[List["Wallet"]] = relationship(back_populates="user", lazy="selectin")
