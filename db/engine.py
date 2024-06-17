from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from .conf import settings

engine = create_async_engine(
    settings.db_url
)

Session = async_sessionmaker(bind=engine, class_=AsyncSession)
