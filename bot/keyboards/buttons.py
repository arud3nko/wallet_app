from enum import Enum


class ReplyButtons:
    Start = "START 🚀"


class WalletActionsButtons(Enum):
    TOP_UP = "Top Up balance 🍋"
    TRANSFER = "Transfer money 🤝"


class InlineButtons(Enum):
    BACK = "⬅️ Back "
    NEW_WALLET = "🆕 Create new wallet"
    ALL_WALLETS = "🚑 Request all wallets"
