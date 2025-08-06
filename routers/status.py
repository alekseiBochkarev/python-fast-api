from fastapi import APIRouter, Depends
from http import HTTPStatus
from repositories import user_repository
from models.db import SessionLocal
from sqlalchemy.orm import Session

from schemas.AppStatus import AppStatus

router = APIRouter(prefix="/api", tags=["Status"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/status", status_code=HTTPStatus.OK)
def status(db: Session = Depends(get_db)) -> AppStatus:
    return AppStatus(users=bool(user_repository.get_total_users_count(db) > 0))
