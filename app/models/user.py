from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    email: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    username: Optional[str] = None


class UserBaseInDB(UserBase):
    id: int = None


# Properties to receive via API on creation
class UserCreate(UserBaseInDB):
    email: str
    password: str


# Properties to receive via API on update
class UserUpdate(UserBaseInDB):
    password: Optional[str] = None


# Additional properties to return via API
class User(UserBaseInDB):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


# Additional properties stored in DB
class UserInDB(UserBaseInDB):
    hashed_password: str
