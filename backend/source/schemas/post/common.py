from fastapi import Query
from pydantic import AliasChoices, BaseModel, Field
from utils.datetime import datetime, utcnow


class Post(BaseModel):
    id: int
    creator_id: int = Field(
        serialization_alias="creatorId",
        validation_alias=AliasChoices("creatorId", "creator_id"),
    )
    created_at: datetime = Field(
        default=utcnow(),
        serialization_alias="createdAt",
        validation_alias=AliasChoices("createdAt", "created_at"),
    )
    updated_at: datetime = Field(
        default=utcnow(),
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updatedAt", "updated_at"),
    )
    title: str
    text: str


class PostFilters(BaseModel):
    creator_id: int | None = Query(
        None,
        validation_alias="creatorId",
    )
