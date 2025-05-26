from enum import StrEnum

PREFIX = "/media"


class EPath(StrEnum):
    UPLOAD = "/upload"
    DOWNLOAD = "/{id}"
    DELETE = "/{id}"
