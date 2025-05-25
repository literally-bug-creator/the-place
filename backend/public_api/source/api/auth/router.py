from fastapi import APIRouter, Depends, status
from schemas.auth import forms, responses
from utils.auth import oauth2_bearer

from .config import PREFIX, EPath
from .service import AuthService

router = APIRouter(prefix=PREFIX, tags=["Auth"])


@router.post(
    path=EPath.REGISTER,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": responses.Register},
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def register(
    form: forms.Register = Depends(forms.register),
    service: AuthService = Depends(AuthService),
):
    return await service.register(form)


@router.post(
    path=EPath.LOGIN,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": responses.Login},
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_401_UNAUTHORIZED: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def login(
    form: forms.Login = Depends(forms.login),
    service: AuthService = Depends(AuthService),
):
    return await service.login(form)


@router.get(
    path=EPath.ME,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": responses.Me},
        status.HTTP_401_UNAUTHORIZED: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def get_me(
    token: str = Depends(oauth2_bearer),
    service: AuthService = Depends(AuthService),
):
    return await service.get_me(token)


@router.post(
    path=EPath.LOGOUT,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {},
    },
)
async def logout(service: AuthService = Depends(AuthService)):
    return await service.logout()