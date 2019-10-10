from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException
from app import crud
from pydantic.types import EmailStr, SecretStr
from sqlalchemy.orm import Session
from app.core import config
from app.api.utils.db import get_db
from app.api.utils.security import get_current_active_user
from app.db_models.user import User as DBUser
from app.models.user import User, UserCreate, UserInDB, UserUpdate

router = APIRouter()

@router.get("/", response_model=List[User])
def read_users(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: DBUser = Depends(get_current_active_user)
):
    """
    Retrieve users
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users

@router.post('/', response_model=User)
def create_user(
    *,
    db: Session = Depends(get_db),
    password: str = Body(...),
    email: EmailStr,
    username: str = Body(None),
):
    """
    Create new user
    """
    if not config.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail='Registration is closed'
        )
    user = crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail='User already exists'
        )
    user_in = UserCreate(password=password, email=email, username=username)
    user = crud.user.create(db, user_in=user_in)
    return user
