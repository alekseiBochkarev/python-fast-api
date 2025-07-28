from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from models.db import SessionLocal
from models.user_models import User
from schemas.user_schemas import UserOut, Support, UserResponse, UsersListResponse

app = FastAPI()


# Зависимость
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    support = Support(
        url="https://contentcaddy.io/?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        text="Tired of writing endless social media content? Let Content Caddy generate it for you."
    )
    return UserResponse(data=user, support=support)


# ✅ Получить всех пользователей с пагинацией
@app.get("/api/users", response_model=UsersListResponse)
def get_users(
        page: int = Query(1, ge=1),
        per_page: int = Query(6, ge=1),
        db: Session = Depends(get_db)
):
    total = db.query(User).count()
    users = (
        db.query(User)
        .offset((page - 1) * per_page)
        .limit(per_page)
        .all()
    )

    total_pages = (total + per_page - 1) // per_page  # округление вверх

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
