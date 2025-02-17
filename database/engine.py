import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from database.models import Base


# Получаем URL из .env
db_url = os.getenv("DB_URL")

# Проверяем, что URL не пустой
if not db_url:
    raise ValueError("Переменная окружения DB_URL не задана!")

# Создаем движок
engine = create_async_engine(db_url, echo=True)

# Создаем фабрику сессий
session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
