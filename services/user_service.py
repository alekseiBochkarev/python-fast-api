from sqlalchemy.orm import Session
from fastapi import HTTPException
from http import HTTPStatus
from repositories import user_repository
from schemas.user_schemas import UsersListResponse, Support, UserResponse, UserCreate, UserOut


def get_user_by_id(user_id: int, db: Session) -> UserResponse:
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid user id")
    user = user_repository.get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")

    support = Support(
        url="https://contentcaddy.io/?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        text="Tired of writing endless social media content? Let Content Caddy generate it for you."
    )

    return UserResponse(data=user, support=support)


def get_users_paginated(page: int, per_page: int, db: Session) -> UsersListResponse:
    total = user_repository.get_total_users_count(db)
    users = user_repository.get_users_paginated(page, per_page, db)

    total_pages = (total + per_page - 1) // per_page

    support = Support(
        url="https://contentcaddy.io/?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        text="Tired of writing endless social media content? Let Content Caddy generate it for you."
    )

    return UsersListResponse(
        page=page,
        per_page=per_page,
        total=total,
        total_pages=total_pages,
        data=users,
        support=support
    )


def create_user(user_data: UserCreate, db: Session) -> UserOut:
    user = user_repository.create_user(user_data, db)
    return UserOut.model_validate(user)


def delete_user(user_id: int, db: Session) -> dict:
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid user id")
    success = user_repository.soft_delete_user(user_id, db)
    if not success:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return {"message": f"User {user_id} deleted"}


