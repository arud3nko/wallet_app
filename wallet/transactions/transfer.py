from ..types.transaction import Transaction
from ..types.wallet import Wallet


class Transfer(Transaction):
    def __init__(self,
                 src: Wallet,
                 dest: Wallet,
                 amount: float):
        super().__init__(src, dest, amount)

    def execute(self) -> None:
        amount = super().amount
        super().src.balance -= amount
        super().dest.balance += amount
