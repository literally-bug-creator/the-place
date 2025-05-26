from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class PostComment(Base):
    __tablename__ = "post_comment"

    creator_id: Mapped[int] = mapped_column(index=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"))
    text: Mapped[str] = mapped_column()
