from enums.post_reaction_type import PostReactionType
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class PostReaction(Base):
    __tablename__ = "post_reactions"

    creator_id: Mapped[int] = mapped_column(index=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"))
    type: Mapped[PostReactionType] = mapped_column(index=True)

    __table_args__ = (
        UniqueConstraint("creator_id", "post_id", name="uix_user_post_reaction"),
    )
