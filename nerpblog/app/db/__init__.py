# import sqlalchemy as db
# from sqlalchemy.orm import Session

# from nerpblog.app.db.tables import Base

# from nerpblog.config import db_connect

# engine = db.create_engine(db_connect, pool_pre_ping=True)
# conn = engine.connect()
# session = Session(engine)

# Base.metadata.create_all(engine)

import asyncio
from nerpblog.config import db_connect
from nerpblog.app.db.models import Base
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

engine = create_async_engine(db_connect)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)



async def get_async_session():
    async with async_session_maker() as session:
        yield session





