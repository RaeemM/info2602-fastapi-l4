from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import select
from app.database import SessionDep
from app.models import *
from app.auth import encrypt_password, verify_password, create_access_token, AuthDep
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import status

cat_router = APIRouter(tags=["Category Management"])

@cat_router.post('/category' response_model=CategoryResponse)
def create_todo(db:SessionDep, user:AuthDep, cat_data:CategoryCreate):
    cat = Category(user_id=user.id, text= cat_data.text)
    try:
        db.add(cat)
        db.commit()
        db.refresh(cat)
        return cat
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="An error occurred while creating an item",
        )