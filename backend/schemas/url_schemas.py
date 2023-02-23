from datetime import datetime
from fastapi import Body
from pydantic import BaseModel

class UrlBase(BaseModel):
    value: str
    
class UrlCreate(UrlBase):
    created_at: datetime | None = Body(default=None)
        
    class Config:
        orm_mode = True
    
class UrlDelete(UrlBase):
    deleted_at: datetime | None = Body(default=None)
    
class UrlGet(UrlBase):
    id: int
    created_at : datetime
    created_by : int
    
    class Config:
        orm_mode = True
            
class Url(UrlBase):
    id: int
    created_at : datetime
    created_by : int
    deleted_at : datetime
    deleted_by : int
    
    class Config:
        orm_mode = True