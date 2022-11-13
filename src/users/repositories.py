from datetime import datetime
from typing import Optional

from databases.interfaces import Record
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update

from src.auth.utils import hash_password
from src.db.base import BaseRepository
from src.users.models import User as users
from src.users.schemas import User
from src.users.schemas import UserIn
from src.users.schemas import UserOut
from src.users.schemas import UserPersonalInfoIn


class UserQueryRepository(BaseRepository):
    async def get(self, limit: int = 100, skip: int = 0) -> list[Record]:
        query = select(users).limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_email(self, email: str) -> Optional[User]:
        query = select(users).where(users.email == email)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def get_by_id(self, id: int) -> Optional[User]:
        query = select(users).where(users.id == id)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)


class UserCommandRepository(BaseRepository):
    async def create(self, u: UserIn) -> UserOut:
        user = User(
            **u.dict(),
            hashed_password=hash_password(u.password),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        values = {**user.dict()}
        values.pop("id", None)
        query = insert(users).values(**values)
        user.id = await self.database.execute(query)
        return UserOut.parse_obj(user)

    async def update(self, id: int, user: UserPersonalInfoIn) -> UserOut:
        user_update = UserPersonalInfoIn(**user.dict())
        values = {
            **user_update.dict(),
            "updated_at": datetime.utcnow(),
        }
        query = update(users).where(users.id == id).values(**values)
        await self.database.execute(query)
        return UserOut(**user_update.dict(), id=id)
