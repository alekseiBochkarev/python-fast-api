from pydantic import BaseModel, HttpUrl, EmailStr
from typing import List, Optional


class UserOut(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl

    model_config = {
        "from_attributes": True
    }


class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    avatar: Optional[HttpUrl] = None  # может быть пустым или отсутствовать


class Support(BaseModel):
    url: HttpUrl
    text: str


class UserResponse(BaseModel):
    data: UserOut
    support: Support


class UsersListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[UserOut]
    support: Support
