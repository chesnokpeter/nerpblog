from datetime import datetime
from pydantic import BaseModel

class CommentSchema(BaseModel):
    id: int
    text: str
    date: datetime
    postid: int
    userid: int

class CommentSchemaExtend(CommentSchema):
    username: str

class AddComment(BaseModel):
    text: str
    postid: int
    tgid: int

class AddCommentExtend(AddComment):
    date: datetime
    userid: int