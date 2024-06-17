from typing import Optional, List

from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Wallet
from ..exceptions import WalletAlreadyExists


async def get_wallet_by_id(
        session: AsyncSession,
        wallet_id: str) -> Optional[Wallet]:
    """
    Provides Wallet instance from DB by wallet unique id

    :param session: `AsyncSession` instance
    :param wallet_id: An unique wallet identifier
    :return: `Wallet` or `None` if it does not exist
    """
    stmt = (select(Wallet)
            .options(selectinload(Wallet.currency))
            .where(wallet_id == Wallet.id))

    result = await session.execute(stmt)

    _wallet: Wallet = result.scalars().first()

    return _wallet


async def get_all_wallets(
        session: AsyncSession) -> List[Wallet]:
    """
    Provides all wallets from DB

    :param session: `AsyncSession` instance
    :return: List of wallets
    """
    stmt = select(Wallet).options(selectinload(Wallet.user))

    result = await session.execute(stmt)

    _wallets: List[Wallet] = [wallet for wallet in result.scalars().all()]

    return _wallets


async def create_wallet(
        session: AsyncSession,
        user_id: int,
        currency_id: int,
        wallet_id: str = uuid4().__str__().split("-")[0]) -> Wallet:
    """
    Saves wallet data to Database

    :param session: `AsyncSession` instance
    :param wallet_id: An unique wallet identifier
    :param user_id: Owner's identifier
    :param currency_id: Currency identifier
    :return: Created `Wallet`
    """

    _wallet = Wallet(
        id=wallet_id,
        balance=0,
        user_id=user_id,
        currency_id=currency_id
    )

    existing = await get_wallet_by_id(session, wallet_id)

    if existing:
        raise WalletAlreadyExists(_wallet)

    session.add(_wallet)
    await session.flush()
    await session.refresh(_wallet)

    return _wallet
