from typing import Callable

from wallet.wallet_handler import WalletHandler
from wallet.core.currency import Currency
from wallet.transactions import TopUpBalance, Transfer
from wallet.types.transaction import TransactionMiddleware, Transaction


class LoggingPreMiddleware(TransactionMiddleware):

    def __call__(self, transaction: Transaction, call_next: Callable):
        print(f"Attempt to make transaction: {transaction}")
        call_next()


class HandleZeroAndMinusTransactionAmount(TransactionMiddleware):

    def __call__(self, transaction: Transaction, call_next: Callable):
        if transaction.amount <= 0:
            print("Incorrect Top Up balance")
            return
        call_next()


class LoggingPostMiddleware(TransactionMiddleware):

    def __call__(self, transaction: Transaction, call_next: Callable):
        print(f"Transaction completed. Destination balance: {transaction.dest.balance}")
        call_next()


rub = Currency("RUB", 95)

eur = Currency("RUB", 110)


handler = WalletHandler()
handler.transaction_handler.add_pre_middleware(LoggingPreMiddleware())
handler.transaction_handler.add_pre_middleware(HandleZeroAndMinusTransactionAmount())
handler.transaction_handler.add_post_middleware(LoggingPostMiddleware())

wallet = handler.new_wallet(rub)

friend_wallet = handler.new_wallet(eur)

birthday_gift = TopUpBalance(wallet, 1113)

trans = Transfer(wallet, friend_wallet, 10000)

handler.provide(birthday_gift)

handler.provide(trans)


print(wallet.balance, friend_wallet.balance)