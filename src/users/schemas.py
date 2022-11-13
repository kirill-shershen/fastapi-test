import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import constr
from pydantic import EmailStr
from pydantic import validator


Password: constr = constr(min_length=8)


class User(BaseModel):
    id: Optional[str] = None
    name: str
    surname: str
    phone: str
    email: EmailStr
    hashed_password: str
    is_stuff: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserIn(BaseModel):
    name: str
    surname: str
    phone: str
    email: EmailStr
    password: Password
    password2: Password
    is_stuff: bool = False

    @validator("password2")
    def password_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("passwords don't match")
        return v


class UserPersonalInfoIn(BaseModel):
    name: str
    surname: str
    phone: str
    email: EmailStr


class UserOut(BaseModel):
    id: int
    name: str
    surname: str
    phone: str
    email: EmailStr
    is_stuff: bool = False

    class Config:
        arbitrary_types_allowed = True
