from pydantic import BaseModel
from typing import List, Union, Any
from datetime import datetime


class PostSchema(BaseModel):
    id: int
    htmltext: str
    title: str
    media: Union[List[str], None]
    date: datetime
    likes: int
    userid: int

class Post_User(PostSchema):
    username: str
    botlink: Union[None, str] = None