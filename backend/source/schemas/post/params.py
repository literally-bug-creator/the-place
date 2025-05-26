from fastapi import Depends, Path
from pydantic import BaseModel
from schemas.common.list import ListParams

from .common import PostFilters


class BaseParams(BaseModel):
    id: int = Path()


class Read(BaseParams): ...


class Update(BaseParams): ...


class Delete(BaseParams): ...


class List(ListParams):
    filters: PostFilters = Depends()
