from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

class User(Base) :
    __tablename__ = "users"
    
    id : int = Column(Integer, primary_key=True, index=True)
    name : str = Column(String, nullable=False)
    username : str = Column(String, nullable=True)
    email : str = Column(String, unique=True, nullable=False, index=True)
    password_hash : str = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
    deleted_at = Column(DateTime, nullable=True)
    