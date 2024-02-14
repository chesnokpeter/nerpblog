import sqlalchemy as db
from sqlalchemy.orm import Session

from nerpblog.app.db.tables import Base

from nerpblog.config import db_connect

engine = db.create_engine(db_connect, pool_pre_ping=True)
conn = engine.connect()
session = Session(engine)

Base.metadata.create_all(engine)
