from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.database import Base
from models.url_model import Url

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    name = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.now)
    
    urls_creator = relationship("Url", back_populates="creator", foreign_keys=[Url.created_by])
    urls_remover = relationship("Url", back_populates="remover", foreign_keys=[Url.deleted_by])