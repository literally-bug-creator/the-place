from fastapi import Body
from pydantic import BaseModel
from utils.datetime import datetime, utcnow


class Create(BaseModel):
    created_at: datetime = Body(default=utcnow())
    title: str = Body()
    text: str = Body()


class Update(BaseModel):
    created_at: datetime | None = Body(default=None)
    title: str | None = Body(default=None)
    text: str | None = Body(default=None)
