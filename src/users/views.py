from fastapi import APIRouter
from fastapi_injector import Injected

from src.auth.exceptions import ForbiddenException
from src.core.exceptions import BadRequest
from src.users.repositories import UserCommandRepository
from src.users.repositories import UserQueryRepository
from src.users.schemas import UserIn
from src.users.schemas import UserOut
from src.users.schemas import UserPersonalInfoIn
from src.users.stories import UpdatePersonalInfoUserStory

users_router = APIRouter()


@users_router.get("/", response_model=list[UserOut])
async def read_users(
    limit: int = 100,
    skip: int = 0,
    users_query: UserQueryRepository = Injected(UserQueryRepository),
):
    return await users_query.get(limit=limit, skip=skip)


@users_router.post("/", response_model=UserOut)
async def create_user(
    user: UserIn,
    users_command: UserCommandRepository = Injected(UserCommandRepository),
):
    return await users_command.create(u=user)


@users_router.put("/", response_model=UserOut)
async def update_user(
    id: int,
    user: UserPersonalInfoIn,
    personal_info_update: UpdatePersonalInfoUserStory = Injected(UpdatePersonalInfoUserStory),
):
    try:
        return await personal_info_update.update(id, user)
    except ForbiddenException as e:
        raise BadRequest(detail=str(e))
