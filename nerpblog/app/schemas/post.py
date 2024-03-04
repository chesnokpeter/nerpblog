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

class PostSchemaExtend(PostSchema):
    username: str
    botlink: Union[None, str] = None 

class AddPost(BaseModel):
    htmltext: str
    title: str
    userid: int
    media: Union[List[str], None]

class AddPostExtend(AddPost):
    date: datetime
    likes: int