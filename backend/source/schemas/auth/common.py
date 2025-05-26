from enums.user_role import EUserRole
from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    nickname: str
    role: EUserRole
