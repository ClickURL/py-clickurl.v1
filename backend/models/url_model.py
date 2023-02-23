from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from db.database import Base

class Url(Base):
    __tablename__ = "url"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    value = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    created_by = Column(Integer, ForeignKey("user.id"))
    deleted_at = Column(DateTime, onupdate=datetime.now)
    deleted_by = Column(Integer, ForeignKey("user.id"))
    
    creator = relationship("User", back_populates="urls_creator", foreign_keys=[created_by])
    remover = relationship("User", back_populates="urls_remover", foreign_keys=[deleted_by])
