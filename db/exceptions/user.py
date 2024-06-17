from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..models import User


class UserORMException(Exception):
    def __init__(self, user: "User"):
        self.user = user


class UserAlreadyExists(UserORMException):
    def __str__(self):
        return f"Error occurred: user with Telegram ID {self.user.tg_id} already exists"


class UserNotFount(UserORMException):
    def __str__(self):
        return f"Error occurred: user with Telegram ID {self.user.tg_id} not found"
