from datetime import datetime
from pydantic import BaseModel

from typing import List, Union, Any

class UserModel(BaseModel):
    id: int
    tgid: int
    name: str
    tglink: str

class PostModel(BaseModel):
    id: int
    htmltext: str
    title: str
    media: Union[List[str], None]
    date: datetime
    likes: int
    userid: int

class PostExtended(PostModel):
    username: str
    botlink: Union[None, str] = None

class AddPost(BaseModel):
    htmltext: str
    title: str
    userid: int
    media: Union[List[str], None]

class AddPostExtended(AddPost):
    date: datetime
    likes: int

class CommentModel(BaseModel):
    id: int
    text: str
    date: datetime
    postid: int
    userid: int

class AddComment(BaseModel):
    text: str
    postid: int
    tgid: int

class AddCommentExtended(AddComment):
    date: datetime
    userid: int

