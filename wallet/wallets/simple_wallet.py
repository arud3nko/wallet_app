from ..types.transaction import Transaction
from ..types.wallet import Wallet


class SimpleWallet(Wallet):

    def do(self, transaction: Transaction) -> None:
        pass