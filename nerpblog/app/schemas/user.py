from pydantic import BaseModel

class UserModel(BaseModel):
    id: int
    tgid: int
    name: str
    tglink: str