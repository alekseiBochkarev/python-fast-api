from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from models.db import SessionLocal
from schemas.user_schemas import UserResponse, UsersListResponse, UserOut, UserCreate
from services.user_service import get_users_paginated, get_user_by_id, create_user, delete_user

router = APIRouter(prefix="/api/users", tags=["Users"])


# Зависимость для подключения к БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(user_id, db)


@router.get("/", response_model=UsersListResponse)
def get_users(
    page: int = Query(1, ge=1),
    per_page: int = Query(6, ge=1),
    db: Session = Depends(get_db)
):
    return get_users_paginated(page, per_page, db)


@router.post("/", response_model=UserOut, status_code=201)
def create_user_endpoint(user_data: UserCreate, db: Session = Depends(get_db)):
    return create_user(user_data, db)


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return delete_user(user_id, db)
