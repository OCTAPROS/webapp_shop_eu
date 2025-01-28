from sqlmodel import Session, create_engine
from core.config import settings

SQLALCHEMY_DATABASE_URL = settings.ORACLE_DB_URL
engine = create_engine(settings.ORACLE_DB_URL)

def get_dbsession():
    with Session(engine) as session:
        yield session
