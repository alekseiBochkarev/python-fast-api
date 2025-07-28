from pydantic import BaseModel, HttpUrl
from typing import List


class UserOut(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: HttpUrl

    model_config = {
        "from_attributes": True
    }


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
