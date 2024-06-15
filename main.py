from typing import Callable

from wallet.wallet_handler import WalletHandler
from wallet.core.currency import Currency
from wallet.transactions import TopUpBalance
from wallet.types.transaction import TransactionMiddleware, Transaction


class LoggingPreMiddleware(TransactionMiddleware):

    def __call__(self, transaction: Transaction, call_next: Callable):
        print(f"Attempt to make transaction: {transaction}")
        call_next()


class LoggingPostMiddleware(TransactionMiddleware):

    def __call__(self, transaction: Transaction, call_next: Callable):
        print(f"Transaction successful. Destination balance: {transaction.dest.balance}")
        call_next()


rub = Currency("RUB", 95)


handler = WalletHandler()
handler.transaction_handler.add_pre_middleware(LoggingPreMiddleware())
handler.transaction_handler.add_post_middleware(LoggingPostMiddleware())

wallet = handler.new_wallet(rub)

birthday_gift = TopUpBalance(wallet, 1113)

handler.do(birthday_gift)
