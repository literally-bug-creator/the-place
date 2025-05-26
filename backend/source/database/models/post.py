from datetime import datetime

from database.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Post(Base):
    __tablename__ = "posts"

    creator_id: Mapped[int] = mapped_column(index=True)
    created_at: Mapped[datetime] = mapped_column()
    title: Mapped[str] = mapped_column()
    # thumbnail: Mapped[str] = mapped_column()
    text: Mapped[str] = mapped_column()
