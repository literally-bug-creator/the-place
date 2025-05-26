from collections.abc import Callable

import aiofiles
from api.auth.config import PREFIX, EPath
from config import get_auth_settings
from database.repos.user import UserRepo
from enums.user_role import EUserRole
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from schemas.auth.common import User

auth_settings = get_auth_settings()
oauth2_bearer = OAuth2PasswordBearer(tokenUrl=PREFIX + EPath.LOGIN)


async def read_key(path: str):
    async with aiofiles.open(path) as key_file:
        return await key_file.read()


async def get_auth_token(request: Request) -> str:
    token = request.headers.get("Authorization")
    if token is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token.split()[-1]


async def get_user(
    token: str = Depends(oauth2_bearer), repo: UserRepo = Depends(UserRepo)
) -> User:
    public_key = await read_key(auth_settings.public_key_path)
    try:
        payload = jwt.decode(token, public_key, [auth_settings.algorithm])
        user_scheme: User = User.model_validate(payload)
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED) from None

    if not await repo.filter_one(**user_scheme.model_dump()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return user_scheme


def get_user_by_min_role(min_role: EUserRole | None = None) -> Callable:
    async def dep(user: User = Depends(get_user)) -> User:
        if (min_role is not None) and (user.role > min_role):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return user

    return dep


def get_user_has_role(roles: list[EUserRole]) -> Callable:
    async def dep(user: User = Depends(get_user)) -> User:
        if user.role not in roles:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        return user

    return dep
