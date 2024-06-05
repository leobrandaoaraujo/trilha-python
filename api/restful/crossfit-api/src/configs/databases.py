from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from configs.settings import settings

engine = create_async_engine(settings.DB_URL, echo=False)
assync_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_session() -> AsyncGenerator:
    async with assync_session as session:
        yield session