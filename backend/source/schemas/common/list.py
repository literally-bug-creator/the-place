from fastapi import Depends
from pydantic import BaseModel

from .pagination import PaginationParams
from .sort import SortParams


class ListParams(BaseModel):
    pagination: PaginationParams = Depends()
    sort: SortParams = Depends()


class ListResponse[T](BaseModel):
    items: list[T]
    total: int
