import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.infrastructure.db.models import Base
from app.config import POSTGRES_HOST as HOST, POSTGRES_PORT as PORT


load_dotenv()
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
db = os.getenv("POSTGRES_DB")

if not user or not password or not db:
    raise EnvironmentError("Some of DB params are not set in .env file. Either user, password or db name")

DATABASE_URL = f"postgresql+asyncpg://{user}:{password}@{HOST}:{PORT}/{db}"

engine = create_async_engine(DATABASE_URL, echo = True)
async_session = sessionmaker(engine, expire_on_commit = False, class_ = AsyncSession)

async def create_session() -> AsyncSession:
    async with async_session() as session:
        return session


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
