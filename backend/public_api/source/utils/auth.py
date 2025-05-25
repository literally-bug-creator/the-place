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


def extract_token_from_header(header_value: str) -> str:
    return header_value.split()[-1]


async def read_key(path: str):
    async with aiofiles.open(path) as key_file:
        return await key_file.read()


def decode_and_validate_token(token: str, public_key: str, algorithm: str) -> User:
    try:
        payload = jwt.decode(token, public_key, [algorithm])
        user_scheme: User = User.model_validate(payload)
        return user_scheme
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED) from None


async def get_auth_token(request: Request) -> str:
    token = request.headers.get("Authorization")
    if token is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return extract_token_from_header(token)


async def get_user(
    token: str = Depends(oauth2_bearer), repo: UserRepo = Depends(UserRepo)
) -> User:
    public_key = await read_key(auth_settings.public_key_path)
    user_scheme = decode_and_validate_token(token, public_key, auth_settings.algorithm)
    if not await repo.filter_one(**user_scheme.model_dump()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user_scheme


def get_user_by_min_role(min_role: EUserRole | None = None) -> Callable:
    async def dependancy(user: User = Depends(get_user)) -> User:
        if (min_role is not None) and (user.role > min_role):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return user

    return dependancy


def get_user_has_role(roles: list[EUserRole]) -> Callable:
    async def dependancy(user: User = Depends(get_user)) -> User:
        if user.role not in roles:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        return user

    return dependancy
