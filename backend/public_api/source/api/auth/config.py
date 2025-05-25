from enum import StrEnum

PREFIX = "/auth/jwt"


class EPath(StrEnum):
    ME = "/me"
    LOGIN = "/login"
    REGISTER = "/register"
    LOGOUT = "/logout"
