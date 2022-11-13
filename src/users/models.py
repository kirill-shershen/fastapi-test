import datetime

import sqlalchemy
from sqlalchemy import Column

from src.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True)
    email = Column(sqlalchemy.String, unique=True)
    name = Column(sqlalchemy.String)
    surname = Column(sqlalchemy.String)
    phone = Column(sqlalchemy.String)
    hashed_password = Column(sqlalchemy.String)
    is_stuff = Column(sqlalchemy.Boolean)
    created_at = Column(sqlalchemy.DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(sqlalchemy.DateTime, default=datetime.datetime.utcnow)
