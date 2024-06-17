from aiogram import F
from aiogram.filters import MagicData


Authorized = MagicData(F.user.authorized)
"""Very simple authorization filter"""
