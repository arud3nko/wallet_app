import asyncio
from typing import Tuple

from aiogram import Bot, Dispatcher
from fastapi import FastAPI
from uvicorn import Config, Server
from bot.app import get_app

from db.engine import engine

from api.bot import BotAPIRoutes
from api.bot import router as bot_api_router

from wallet.wallet_handler import WalletHandler
from middlewares import LoggingPostMiddleware


def setup_bot() -> Tuple[Bot, Dispatcher]:
    """Setting up bot's params"""
    handler = WalletHandler()
    bot, dp = get_app(handler)

    handler.transaction_handler.add_post_middleware(LoggingPostMiddleware())

    bot_api_router.bot = bot
    bot_api_router.session_engine = engine

    return bot, dp


def setup_app() -> FastAPI:
    """Setting up API"""
    app = FastAPI()
    app.include_router(bot_api_router, prefix=BotAPIRoutes.PREFIX)

    return app


async def start_app(bot: Bot, dp: Dispatcher, app: FastAPI):
    """Starting app locally using Uvicorn"""
    config = Config(app, host="127.0.0.1", port=8000, loop="asyncio")
    server = Server(config)

    polling_task = asyncio.create_task(dp.start_polling(bot))
    server_task = asyncio.create_task(server.serve())

    await asyncio.gather(polling_task, server_task)


def main():
    """Entry point"""
    bot, dp = setup_bot()
    app = setup_app()
    asyncio.run(start_app(bot, dp, app))


if __name__ == "__main__":
    main()
