from enum import StrEnum

PREFIX = "/post"


class EPath(StrEnum):
    CREATE = "/"
    READ = "/{id}"
    UPDATE = "/{id}"
    DELETE = "/{id}"
