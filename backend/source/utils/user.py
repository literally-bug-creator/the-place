from schemas.auth.common import EUserRole, User


def get_role(user: User) -> EUserRole:
    return user.role


def has_role(user: User, role: EUserRole) -> bool:
    return get_role(user) == role


def has_roles(user: User, roles: list[EUserRole]) -> bool:
    return any(has_role(user, role) for role in roles)


def has_min_role(user: User, role: EUserRole) -> bool:
    user_role = get_role(user)
    return user_role >= role
