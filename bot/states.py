from aiogram.fsm.state import State, StatesGroup


class AuthStates(StatesGroup):
    """
    Authorization states
    """
    entering_passcode = State()


class TopUpBalance(StatesGroup):
    """Top Up states"""
    entering_amount = State()
