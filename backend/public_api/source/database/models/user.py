from database.models.base import Base
from enums.user_role import EUserRole


class User(Base):
    email: str  # TODO: Add index
    name: str
    surname: str
    hashed_password: str
    role: EUserRole
