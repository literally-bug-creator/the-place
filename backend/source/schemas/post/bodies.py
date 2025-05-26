from pydantic import BaseModel
from utils.datetime import datetime, utcnow


class Create(BaseModel):
    created_at: datetime = utcnow()
    updated_at: datetime = utcnow()
    title: str
    text: str


class Update(BaseModel):
    title: str | None = None
    text: str | None = None
