from dataclasses import dataclass

from injector import inject

from src.auth.exceptions import ForbiddenException
from src.users.repositories import UserCommandRepository
from src.users.repositories import UserQueryRepository
from src.users.schemas import User
from src.users.schemas import UserOut
from src.users.schemas import UserPersonalInfoIn


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
