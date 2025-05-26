from collections.abc import AsyncIterator
import os
from typing import no_type_check

MISSING_DATABASE_URL = "DATABASE_URL is not set"

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


def get_db_url() -> str:
    url = os.getenv("DATABASE_URL")
    if url is None:
        raise ValueError(MISSING_DATABASE_URL)
    return url


def get_db_engine() -> AsyncEngine:
    return create_async_engine(
        get_db_url(),
        pool_size=20,
        max_overflow=20,
        pool_timeout=30,
        pool_recycle=1800,
    )


@no_type_check
async def get_session() -> AsyncIterator[AsyncSession]:
    async_session = sessionmaker(
        bind=get_db_engine(),
        class_=AsyncSession,
        expire_on_commit=False,
    )
    async with async_session() as session:
        yield session
