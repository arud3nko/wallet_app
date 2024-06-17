from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Currency


async def get_currency_by_code(
        session: AsyncSession,
        code: str) -> Optional[Currency]:
    """
    Provides Currency instance from DB by currency id

    :param session: `AsyncSession` instance
    :param code: Currency code
    :return: `Currency` or `None` if it does not exist
    """
    stmt = (select(Currency)
            .options(selectinload(Currency.wallets))
            .where(code == Currency.code))

    result = await session.execute(stmt)

    _currency: Currency = result.scalars().first()

    return _currency


async def get_all_currencies(
        session: AsyncSession) -> List[Currency]:
    """
    Provides all currencies from DB

    :param session: `AsyncSession` instance
    :return: List of currencies
    """
    stmt = select(Currency).options(selectinload(Currency.wallets))

    result = await session.execute(stmt)

    _currencies: List[Currency] = [currency for currency in result.scalars().all()]

    return _currencies


async def create_currency(
        session: AsyncSession,
        code: str,
        rate: float) -> Currency:
    """
    Saves wallet data to Database

    :param session: `AsyncSession` instance
    :param code: Currency code
    :param rate: Currency rate
    :return: Created `Currency`
    """

    _currency = Currency(
        code=code,
        rate=rate
    )

    existing = await get_currency_by_code(session, code)

    if existing:
        # raise WalletAlreadyExists(_currency)
        pass

    session.add(_currency)
    await session.flush()
    await session.refresh(_currency)

    return _currency
