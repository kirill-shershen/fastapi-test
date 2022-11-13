from fastapi import APIRouter
from fastapi import HTTPException
from fastapi_injector import Injected
from injector import inject
from starlette import status

from src.auth.schemas import Login
from src.auth.schemas import Token
from src.auth.utils import create_access_token
from src.auth.utils import verify_password
from src.users.repositories import UserQueryRepository

auth_router = APIRouter()


@auth_router.post("/", response_model=Token)
async def login(
    login: Login,
    users: UserQueryRepository = Injected(UserQueryRepository),
):
    user = await users.get_by_email(login.email)
    if user is None or not verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    return Token(access_token=create_access_token({"sub": user.email}), token_type="Bearer")
