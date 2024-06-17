from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..models import Wallet


class WalletORMException(Exception):
    def __init__(self, wallet: "Wallet"):
        self.wallet = wallet


class WalletAlreadyExists(WalletORMException):
    def __str__(self):
        return f"Error occurred: user with Telegram ID {self.wallet.id} already exists"
