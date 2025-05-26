from fastapi import APIRouter, Depends, status

from .config import PREFIX, EPath
from .service import MediaService

router = APIRouter(prefix=PREFIX, tags=["Media"])


@router.post(
    path=EPath.UPLOAD,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": ...},
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def upload(
    service: MediaService = Depends(MediaService),
):
    return await service.upload()


@router.get(
    path=EPath.DOWNLOAD,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": ...},
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_404_NOT_FOUND: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def download(
    service: MediaService = Depends(MediaService),
):
    return await service.download()


@router.delete(
    path=EPath.DELETE,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {"model": ...},
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_404_NOT_FOUND: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def delete(
    service: MediaService = Depends(MediaService),
):
    return await service.delete()
