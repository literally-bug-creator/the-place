from enums.user_role import EUserRole


class User:
    id: int
    email: str
    nickname: str
    role: EUserRole
