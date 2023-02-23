from typing import List

from schemas import user_schemas
from schemas import url_schemas


class UrlGetWithUser(url_schemas.UrlGet):
    creator: user_schemas.UserBase
