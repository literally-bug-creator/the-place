from database.models.post import Post
from database.repos.base import BaseRepo


class PostRepo(BaseRepo):
    MODEL = Post
