from schemas.common.crud import CRUDResponse
from schemas.common.list import ListResponse

from .common import Post

Create = CRUDResponse[Post]
Read = CRUDResponse[Post]
Update = CRUDResponse[Post]
Delete = CRUDResponse[Post]
List = ListResponse[Post]
