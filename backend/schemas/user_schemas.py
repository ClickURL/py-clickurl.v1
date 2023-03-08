from datetime import datetime
from pydantic import BaseModel
from fastapi import Body

class UserBase(BaseModel):
    name: str
    
    class Config:
        orm_mode = True
    
class UserCreate(UserBase):
    created_at: datetime | None = Body(default=None)

class User(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True
