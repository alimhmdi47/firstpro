from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from fastapi import Depends
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio.session import Session

DATABASE_URL = "postgresql+asyncpg://postgres:2005ali.mhmdi@localhost/firstdb"
engine = create_async_engine(DATABASE_URL, echo=True)

async_session = async_sessionmaker(engine,class_=AsyncSession ,expire_on_commit=False)

async def get_session():
    async with async_session() as session:
        yield session
# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)
# def get_session():
#     with Session(engine) as session:
#         yield session
