from database.models.post_comment import PostComment
from database.repos.base import BaseRepo


class PostCommentRepo(BaseRepo):
    MODEL = PostComment
