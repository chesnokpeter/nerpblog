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