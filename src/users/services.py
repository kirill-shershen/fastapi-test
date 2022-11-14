from dataclasses import dataclass
from typing import Optional

from injector import inject

from src.logger import logger
from src.users.repositories import UserQueryRepository
from src.users.schemas import User


@inject
@dataclass
class UserLookupService:
    user_query_repository: UserQueryRepository

    async def is_user_exist_by_email(self, email: str) -> bool:
        user = await self.get_by_email(email)
        logger.warning(f"{user}")
        if user is None:
            return False

        return True

    async def get_by_email(self, email: str) -> Optional[User]:
        return await self.user_query_repository.get_by_email(email)
