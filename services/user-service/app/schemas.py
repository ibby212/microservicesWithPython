from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserOut(BaseModel):
    id: str
    username: str
    email: str
    bio: Optional[str] = None
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class UserList(BaseModel):
    items: list[UserOut]
    total: int
    limit: int
    offset: int
