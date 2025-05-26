from collections.abc import AsyncGenerator, Iterable
from contextlib import asynccontextmanager
from typing import Any

from database import get_session
from database.models.base import Base
from fastapi import Depends
from schemas.common.list import ListParams
from schemas.common.pagination import PaginationParams
from schemas.common.sort import SortOrder, SortParams
from sqlalchemy import Select, exc, exists, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import make_transient


class BaseRepo[ModelT: Base]:
    MODEL: type[ModelT] = None  # type: ignore

    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session

    @property
    def model(self) -> type[ModelT]:
        if self.MODEL is None:
            raise ValueError("MODEL not set")
        return self.MODEL

    async def execute(self, query: Any) -> Any:
        async with self._start_session():
            return await self.session.execute(query)

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()

    async def expunge(self, obj: ModelT) -> None:
        async with self._start_session():
            self.session.expunge(obj)

    async def copy(self, obj: ModelT) -> ModelT | None:
        make_transient(obj)
        delattr(obj, "id")
        return await self.create(obj)

    def add(self, obj: ModelT) -> None:
        self.session.add(obj)

    async def new(self, **data: Any) -> ModelT | None:
        obj = self.model(**data)
        return await self.create(obj)

    async def create(self, obj: ModelT) -> ModelT | None:
        async with self._start_session():
            self.session.add(obj)
            try:
                await self.session.commit()
            except exc.IntegrityError as e:
                print(e)
                await self.rollback()
                return None
        async with self._start_session():
            await self.session.refresh(obj)
        return obj

    async def get(self, id: int) -> ModelT | None:
        async with self._start_session():
            return await self.filter_one(self.model.id == id)

    async def filter(self, *where: Any, **filters: Any) -> Iterable[ModelT] | Any:
        query = self._get_query().where(*where).filter_by(**filters)
        return (await self.execute(query)).scalars()

    async def filter_one(self, *where: Any, **filters: Any) -> ModelT | None | Any:
        query = self._get_query().where(*where).filter_by(**filters)
        return (await self.execute(query)).scalar_one_or_none()

    async def count(self, **filters: Any) -> int | Any:
        query = self._get_query(func.count(self.model.id)).filter_by(**filters)
        return (await self.execute(query)).scalar_one()

    async def is_empty(self) -> bool:
        async with self._start_session():
            exists_query = select(exists().where(self.model.id.isnot(None)))
            result = await self.session.scalar(exists_query)
            return not result

    async def update(self, obj: ModelT, **kwargs: Any) -> ModelT | None:
        async with self._start_session():
            for key, value in kwargs.items():
                setattr(obj, key, value)
            try:
                await self.session.commit()
            except exc.IntegrityError:
                await self.rollback()
                return None
        async with self._start_session():
            await self.session.refresh(obj)
        return obj

    async def delete(self, obj: ModelT) -> None:
        async with self._start_session():
            await self.session.delete(obj)
            await self.commit()

    async def list(
        self, params: ListParams, **filters: Any
    ) -> tuple[Iterable[ModelT], int]:
        query = self._get_query().filter_by(**filters)
        total = await self.count(**filters)
        query = self._apply_sort(query, params.sort)
        query = self._apply_pagination(query, params.pagination)
        items = (await self.execute(query)).scalars()
        return items, total

    def _apply_sort(self, query: Select[Any], params: SortParams) -> Any:
        if params.field is None:
            return query
        field = getattr(self.model, params.field, None)
        if field is None:
            return query
        sorting_field = field.asc() if params.order == SortOrder.Asc else field.desc()
        return query.order_by(sorting_field)

    def _apply_pagination(self, query: Select[Any], params: PaginationParams) -> Any:
        limit = params.per_page
        offset = (params.page - 1) * limit
        return query.limit(limit).offset(offset)

    def _get_query(self, select_data: Any = None) -> Select[Any]:
        if select_data is None:
            select_data = self.model
        return select(select_data)

    @asynccontextmanager
    async def _start_session(self) -> AsyncGenerator[AsyncSession, None]:
        if self.session.is_active:
            yield self.session
            return
        async with self.session.begin():
            yield self.session

    def check_sort(self, params: SortParams) -> bool:
        if params.field is None:
            return True
        return self.contains_field(params.field)

    def contains_field(self, field: str) -> bool:
        return self.model.__table__.columns.get(field) is not None
