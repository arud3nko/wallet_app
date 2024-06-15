from ..types.transaction import Transaction
from ..types.wallet import Wallet


class TopUpBalance(Transaction):
    def __init__(self,
                 dest: Wallet,
                 amount: float):
        super().__init__(None, dest, amount)

    def execute(self) -> None:
        super().dest.balance += super().amount

