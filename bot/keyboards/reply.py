from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

from .buttons import ReplyButtons


def start_keyboard_factory() -> ReplyKeyboardMarkup:
    """
    Returns `ReplyKeyboardMarkup` instance with `Start` button

    :return: `ReplyKeyboardMarkup` instance
    """
    _keyboard = [
        [
            KeyboardButton(text=ReplyButtons.Start)
        ]
    ]

    return ReplyKeyboardMarkup(keyboard=_keyboard, resize_keyboard=True)

