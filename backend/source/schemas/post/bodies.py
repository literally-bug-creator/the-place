from datetime import datetime

from fastapi import Body
from pydantic import BaseModel


class Create(BaseModel):
    creator_id: int = Body()
    created_at: datetime = Body()
    title: str = Body()
    text: str = Body()


class Update(BaseModel):
    creator_id: int | None = Body()
    created_at: datetime | None = Body()
    title: str | None = Body()
    text: str | None = Body()
