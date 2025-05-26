from database.repos.post import PostRepo
from fastapi import Depends
from schemas.post import params, responses


class PostService:
    def __init__(self, repo: PostRepo = Depends()) -> None:
        self._repo = repo

    async def create(self) -> responses.Create: ...

    async def read(self) -> responses.Read: ...

    async def update(self) -> responses.Update: ...

    async def delete(self, pms: params.Delete) -> responses.Delete: ...
