from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from database import Base

class Note(Base):
    __tablename__ = "notes_new"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)
    user_id = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    pinned = Column(Boolean, default=False)
