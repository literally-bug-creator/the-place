from typing import Annotated

from fastapi import APIRouter, Depends, status
from schemas.post import bodies, params, responses

from .config import PREFIX, EPath
from .service import PostService

router = APIRouter(prefix=PREFIX, tags=["Post"])


@router.post(
    path=EPath.CREATE,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": responses.Create},
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def create(
    body: Annotated[bodies.Create, Depends()],
    service: Annotated[PostService, Depends(PostService)],
) -> responses.Create:
    return await service.create(body)


@router.get(
    path=EPath.READ,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": responses.Read},
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_404_NOT_FOUND: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def read(
    pms: Annotated[params.Read, Depends()],
    service: Annotated[PostService, Depends(PostService)],
) -> responses.Read:
    return await service.read(pms)


@router.patch(
    path=EPath.UPDATE,
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        status.HTTP_202_ACCEPTED: {"model": responses.Update},
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_404_NOT_FOUND: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def update(
    pms: Annotated[params.Update, Depends()],
    body: Annotated[bodies.Update, Depends()],
    service: Annotated[PostService, Depends(PostService)],
) -> responses.Update:
    return await service.update(pms, body)


@router.delete(
    path=EPath.DELETE,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {},
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_404_NOT_FOUND: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def delete(
    pms: Annotated[params.Delete, Depends()],
    service: Annotated[PostService, Depends()],
) -> None:
    return await service.delete(pms)
