from database.repos.post import PostRepo
from fastapi import Depends
from schemas.post import bodies, params, responses


class PostService:
    def __init__(self, repo: PostRepo = Depends()) -> None:
        self._repo = repo

    async def create(self, body: bodies.Create) -> responses.Create: ...

    async def read(self, pms: params.Read) -> responses.Read: ...

    async def update(
        self, pms: params.Update, body: bodies.Update
    ) -> responses.Update: ...

    async def delete(self, pms: params.Delete) -> None: ...
