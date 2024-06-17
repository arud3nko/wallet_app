from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession


from ..models import User
from ..exceptions import UserAlreadyExists


async def get_user_by_tg_id(
        session: AsyncSession,
        tg_id: int) -> Optional[User]:
    """
    Provides User instance from DB by telegram id

    :param session: `AsyncSession` instance
    :param tg_id: A telegram user id
    :return: `User` or `None` if it does not exist
    """
    stmt = (select(User)
            .options(selectinload(User.wallets))
            .where(tg_id == User.tg_id))

    result = await session.execute(stmt)

    _user: User = result.scalars().first()

    return _user


async def get_all_users(
        session: AsyncSession) -> List[User]:
    """
    Provides all users from DB

    :param session: `AsyncSession` instance
    :return: List of users
    """
    stmt = select(User).options(selectinload(User.wallets))

    result = await session.execute(stmt)

    _users: List[User] = [user for user in result.scalars().all()]

    return _users


async def create_user(
        session: AsyncSession,
        tg_id: int,
) -> User:
    """
    Saves user's data to Database

    :param session: `AsyncSession` instance
    :param tg_id: A telegram user id
    :return: Created `User`
    """

    _user = User(
        tg_id=tg_id
    )

    existing = await get_user_by_tg_id(session, tg_id)

    if existing:
        raise UserAlreadyExists(_user)

    session.add(_user)
    await session.flush()
    await session.refresh(_user)

    return _user
