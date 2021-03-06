from db.postgres.config import async_session
from sqlalchemy.ext.asyncio import AsyncSession


async def get_session() -> AsyncSession:
    async with async_session() as session:
        async with session.begin():
            yield session
