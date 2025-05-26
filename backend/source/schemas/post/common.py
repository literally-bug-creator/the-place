from datetime import datetime

from fastapi import Query
from pydantic import AliasChoices, BaseModel, Field


class Post(BaseModel):
    id: int
    creator_id: int = Field(
        serialization_alias="creatorId",
        validation_alias=AliasChoices("creatorId", "creator_id"),
    )
    created_at: datetime = Field(
        serialization_alias="createdAt",
        validation_alias=AliasChoices("createdAt", "created_at"),
    )
    title: str
    text: str


class PostFilters(BaseModel):
    creator_id: int | None = Query(
        None,
        validation_alias="creatorId",
    )
    created_at: datetime | None = Query(
        None,
        validation_alias="createdAt",
    )
