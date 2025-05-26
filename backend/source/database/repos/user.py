from database.models.user import User
from database.repos.base import BaseRepo


class UserRepo(BaseRepo):
    MODEL = User
