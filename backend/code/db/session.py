from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker, Session
from core.config import settings
from typing import Generator

SQLALCHEMY_DATABASE_URL = settings.ORACLE_DB_URL

engine = create_engine(settings.ORACLE_DB_URL)

SESSION_LOCAL = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SESSION_LOCAL()
        yield db
    finally:
        db.close()
