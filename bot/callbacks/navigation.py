from aiogram import types, Dispatcher, F

from db.models import User

from ..handlers.core import render_main_menu

from ..keyboards.callback import BackButtonCallbackData, BackButtonActions


async def back_to_main_menu(
        query: types.CallbackQuery,
        user: User
):
    """
    Handles `Back` button
    """

    text, markup = await render_main_menu(user)
    await query.message.edit_text(
        text=text,
        reply_markup=markup
    )
    await query.answer()


def setup(dp: Dispatcher) -> Dispatcher:
    dp.callback_query.register(back_to_main_menu, BackButtonCallbackData.
                               filter(F.a == BackButtonActions.RENDER_MAIN_MENU))
    return dp
