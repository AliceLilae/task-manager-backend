from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    username: Optional[str] = None
    email: str
    password_hash: str


class UserResponse(BaseModel):
    id: int
    name: str
    username: Optional[str] = None
    email: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password_hash: Optional[str] = None