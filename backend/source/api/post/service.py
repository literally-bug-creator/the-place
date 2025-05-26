from database.repos.post import PostRepo
from fastapi import Depends, HTTPException, status
from schemas.auth.common import EUserRole, User
from schemas.post import bodies, common, params, responses
from utils import user as user_utils
from utils.auth import get_user
from utils.datetime import utcnow


class PostService:
    def __init__(
        self, repo: PostRepo = Depends(), user: User = Depends(get_user)
    ) -> None:
        self._repo = repo
        self._user = user

    async def create(self, body: bodies.Create) -> responses.Create:
        if not user_utils.has_le_role(self._user, EUserRole.ADMIN):
            raise HTTPException(status.HTTP_403_FORBIDDEN)

        if not (
            post := await self._repo.new(
                creator_id=self._user.id,
                created_at=body.created_at,
                updated_at=body.updated_at,
                title=body.title,
                text=body.text,
            )
        ):
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE)

        return responses.Create(
            item=common.Post.model_validate(post, from_attributes=True)
        )

    async def read(self, pms: params.Read) -> responses.Read:
        if not (post := await self._repo.get(pms.id)):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return responses.Create(
            item=common.Post.model_validate(post, from_attributes=True)
        )

    async def update(self, pms: params.Update, body: bodies.Update) -> responses.Update:
        if not user_utils.has_le_role(self._user, EUserRole.ADMIN):
            raise HTTPException(status.HTTP_403_FORBIDDEN)

        if not (post_to_update := await self._repo.get(pms.id)):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        updates = body.model_dump(exclude_none=True)

        if not (upd_post := await self._repo.update(post_to_update, **updates, updated_at=utcnow())):
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE)

        return responses.Update(
            item=common.Post.model_validate(upd_post, from_attributes=True)
        )

    async def delete(self, pms: params.Delete) -> None:
        if not user_utils.has_le_role(self._user, EUserRole.ADMIN):
            raise HTTPException(status.HTTP_403_FORBIDDEN)

        if not (post_to_delete := await self._repo.get(pms.id)):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        await self._repo.delete(post_to_delete)
