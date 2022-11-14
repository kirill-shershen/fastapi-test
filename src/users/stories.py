from dataclasses import dataclass

from injector import inject

from src.auth.exceptions import ForbiddenException
from src.auth.schemas import Token
from src.auth.utils import encode_access_token
from src.auth.utils import encode_refresh_token
from src.logger import logger
from src.users.Exceptions import UserCreateError
from src.users.Exceptions import UserIsExist
from src.users.repositories import UserCommandRepository
from src.users.repositories import UserQueryRepository
from src.users.schemas import UserIn
from src.users.schemas import UserOut
from src.users.schemas import UserPersonalInfoIn
from src.users.services import UserLookupService


@inject
@dataclass
class UpdatePersonalInfoUserStory:
    users_query: UserQueryRepository
    users_command: UserCommandRepository

    async def update(
        self,
        id: int,
        user: UserPersonalInfoIn,
    ) -> UserOut:
        old_user = await self.users_query.get_by_id(id=id)
        if old_user is None:
            raise ForbiddenException(detail="Invalid User")
        return await self.users_command.update(id=id, user=user)


@inject
@dataclass
class SignUpStory:
    user_lookup_service: UserLookupService
    user_command_repository: UserCommandRepository

    async def register(self, user: UserIn):
        is_exist_account = await self.user_lookup_service.is_user_exist_by_email(user.email)
        if is_exist_account:
            raise UserIsExist(f"User with email: {user.email} already exists")

        if user.password != user.password2:
            raise UserCreateError("Password mismatch")

        new_user = await self.user_command_repository.create(u=user)
        logger.info(f"{new_user=}")
        return Token(
            access_token=encode_access_token(user.email),
            refresh_token=encode_refresh_token(user.email),
            token_type="Bearer",
        )
