from datetime import datetime
from pydantic import BaseModel

class UserModel(BaseModel):
    id: int
    tgid: int
    name: str
    tglink: str

class PostModel(BaseModel):
    id: int
    htmltext: str
    title: str
    date: datetime
    likes: int
    userid: int

class AddPost(BaseModel):
    htmltext: str
    title: str
    userid: int

class AddPostExtended(AddPost):
    date: datetime
    likes: int