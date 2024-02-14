from typing import Any, List, Union
from datetime import datetime

from sqlalchemy import inspect, BigInteger, ForeignKey, DateTime, Integer, String, DateTime, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from nerpblog.app.models import PostModel, UserModel

class Base(DeclarativeBase):
    def __repr__(self):
        mapper = inspect(self).mapper
        ent = []
        for col in [*mapper.column_attrs]:
            ent.append("{0}={1}".format(col.key, getattr(self, col.key)))
        return "<{0}(".format(self.__class__.__name__) + ", ".join(ent) + ")>"

class USER(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer(), unique=True, primary_key=True, autoincrement=True, nullable=False)
    tgid: Mapped[int] = mapped_column(BigInteger(), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(), nullable=False, primary_key=True) 
    tglink: Mapped[str] = mapped_column(String(), nullable=False) 
    def get_attributes_dict(self) -> dict[str, Any]:
        return UserModel(
            id = self.id,
            tgid = self.tgid,
            name = self.name,
            tglink = self.tglink,
        )

class POST(Base):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(Integer(), unique=True, primary_key=True, autoincrement=True, nullable=False)
    htmltext: Mapped[str] = mapped_column(String(), nullable=False)
    title: Mapped[str] = mapped_column(String(), nullable=False, default='Стандартный заголовок')
    media: Mapped[Union[List[str], None]] = mapped_column(ARRAY(String()), nullable=True)
    date: Mapped[DateTime] = mapped_column(DateTime(), nullable=False, default=datetime.now())
    likes: Mapped[int] = mapped_column(Integer(), nullable=False, default=0)
    userid: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    def get_attributes_dict(self) -> dict[str, Any]:
        return PostModel(
            id = self.id,
            htmltext = self.htmltext,
            title = self.title,
            media = self.media,
            date = self.date,
            likes = self.likes,
            userid = self.userid
        )

