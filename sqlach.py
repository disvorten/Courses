import asyncio

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/demo"


async def async_main():
    engine = create_async_engine(DATABASE_URL, echo=True, future=True)

    async with engine.connect() as conn:
        result = await conn.execute(text("select 1"))

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(async_main())
