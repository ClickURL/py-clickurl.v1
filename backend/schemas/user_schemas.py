from datetime import datetime
from pydantic import BaseModel
from fastapi import Body

import schemas.url_schemas as url_schemas

class UserBase(BaseModel):
    name: str
    
    class Config:
        orm_mode = True
    
class UserCreate(UserBase):
    created_at: datetime | None = Body(default=None)

class User(UserBase):
    id: int
    created_at: datetime
    urls_creator: list[url_schemas.UrlBase] = []
    
    class Config:
        orm_mode = True
