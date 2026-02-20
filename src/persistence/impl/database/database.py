from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from src.core.settings import settings
import psycopg2

sync_engine = create_engine(
    settings.database_settings.url,
    echo=False
)

session_factory = sessionmaker(bind=sync_engine, autoflush=False, autocommit=False)

async_database_url = settings.database_settings.url.replace("postgresql://", "postgresql+asyncpg://")

async_engine = create_async_engine(
    async_database_url,
    echo=False
)

async_session_factory = async_sessionmaker(bind=async_engine, autoflush=False, autocommit=False)

class Base(DeclarativeBase):

    repr_first_cols:int = 3
    repr_cols:tuple[str] = tuple()

    def __repr__(self):
        """Readable representation for debugging"""
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_first_cols:
                cols.append(f"{col}={getattr(self, col)}")
        return f"<{self.__class__.__name__} {', '.join(cols)}>"

