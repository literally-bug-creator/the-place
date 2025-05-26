from database.models.post_reaction import PostReaction
from database.repos.base import BaseRepo


class PostReactionRepo(BaseRepo):
    MODEL = PostReaction
