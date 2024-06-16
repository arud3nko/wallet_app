from ..types.transaction import Transaction


class TransactionException(Exception):
    def __init__(self, transaction: Transaction):
        self.transaction = transaction


class IncompatibleCurrencies(TransactionException):
    def __str__(self):
        return (f"Error occurred while trying to transfer balance between incompatible currency wallets "
                f"({self.transaction.src.currency} to {self.transaction.dest.currency}): "
                f"{self.transaction}")


class NotEnoughBalance(TransactionException):
    def __str__(self):
        return (f"Error occurred while trying to transfer "
                f"{self.transaction.amount} {self.transaction.src.currency} "
                f"from wallet with balance {self.transaction.src.balance} {self.transaction.src.currency}: "
                f"{self.transaction}")
