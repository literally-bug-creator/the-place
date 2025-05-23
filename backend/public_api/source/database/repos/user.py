from database.models.user import User
from database.repos.base import Base


class UserRepo(Base):
    MODEL = User
