from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from fastapi_injector import Injected
from starlette import status

from src.auth.schemas import Login
from src.auth.schemas import Token
from src.auth.utils import decode_refresh_token
from src.auth.utils import encode_access_token
from src.auth.utils import encode_refresh_token
from src.auth.utils import verify_password
from src.core.exceptions import BadRequest
from src.users.repositories import UserQueryRepository
from src.users.schemas import UserIn
from src.users.stories import SignUpStory

auth_router = APIRouter()
security = HTTPBearer()


@auth_router.post("/signin", response_model=Token)
async def login(
    login: Login,
    users: UserQueryRepository = Injected(UserQueryRepository),
):
    user = await users.get_by_email(login.email)
    if user is None or not verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    return Token(
        access_token=encode_access_token(user.email),
        refresh_token=encode_refresh_token(user.email),
        token_type="Bearer",
    )


@auth_router.post("/signup", response_model=Token)
async def signup(user: UserIn, sign_up_story: SignUpStory = Injected(SignUpStory)):
    try:
        return await sign_up_story.register(user)
    except Exception as e:
        raise BadRequest(detail=str(e))


@auth_router.get("/refresh_token")
async def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    try:
        refresh_token = credentials.credentials
        return {"access_token": decode_refresh_token(refresh_token)}
    except Exception as e:
        raise BadRequest(detail=str(e))
