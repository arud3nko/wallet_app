from typing import Tuple

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage


from . import middlewares, handlers, callbacks
from .conf import settings

from wallet.wallet_handler import WalletHandler


def get_app(handler: WalletHandler) -> Tuple[Bot, Dispatcher]:
    """
    Initializes & returns `Bot` & `Dispatcher`
    """

    bot = Bot(token=settings.TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    middlewares.setup(dp, handler)
    handlers.setup(dp)
    callbacks.setup(dp)

    return bot, dp
