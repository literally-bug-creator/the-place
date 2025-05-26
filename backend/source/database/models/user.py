from enums.user_role import EUserRole
from sqlalchemy import Index
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(index=True)
    nickname: Mapped[str] = mapped_column(index=True)
    hashed_password: Mapped[bytes] = mapped_column()
    role: Mapped[EUserRole] = mapped_column()

    __table_args__ = (
        Index("email_index", "email", postgresql_using="hash"),
        Index("nickname_index", "nickname", postgresql_using="hash"),
    )
