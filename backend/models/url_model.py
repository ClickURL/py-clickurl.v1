from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from db.database import Base

class Url(Base):
    __tablename__ = "urls"
    
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    created_by = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime, onupdate=datetime.now)
    deleted_by = Column(Integer, ForeignKey("users.id"))
    
    creator = relationship("User", back_populates="urls_created", foreign_keys=[created_by])
    remover = relationship("User", back_populates="urls_removed", foreign_keys=[deleted_by])
