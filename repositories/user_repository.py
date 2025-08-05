from sqlalchemy.orm import Session
from models.user_models import User
from typing import List, Optional, Type

from schemas.user_schemas import UserCreate


def get_user_by_id(user_id: int, db: Session) -> Optional[User]:
    return db.query(User).filter(User.id == user_id, User.is_deleted == False).first()


def get_users_paginated(page: int, per_page: int, db: Session) -> list[Type[User]]:
    return (
        db.query(User)
        .filter(User.is_deleted == False)
        .offset((page - 1) * per_page)
        .limit(per_page)
        .all()
    )


def get_total_users_count(db: Session) -> int:
    return db.query(User).filter(User.is_deleted == False).count()


def create_user(user_data: UserCreate, db: Session) -> User:
    new_user = User(
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        avatar=user_data.avatar or ""  # если None — сохраняем как пустую строку
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def soft_delete_user(user_id: int, db: Session) -> bool:
    user = db.query(User).filter(User.id == user_id, User.is_deleted == False).first()
    if not user:
        return False
    user.is_deleted = True
    db.commit()
    return True
