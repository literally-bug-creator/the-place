import bcrypt
import jwt


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def is_password_valid(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password)


async def generate_token(payload: dict, private_key: str, algorithm: str) -> str:
    return jwt.encode(payload, private_key, algorithm)


async def decode_token(token: str, public_key: str, algorithms: list) -> dict:
    return jwt.decode(token, public_key, algorithms) 