from databases import Database
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base

from src.config.settings import settings

database = Database(url=settings.database_url)
metadata = MetaData()
engine = create_async_engine(
    settings.database_url,
)
Base = declarative_base()


class BaseRepository:
    def __init__(self, database: Database = database):
        self.database = database
