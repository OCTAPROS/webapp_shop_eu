import enum
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship, create_engine, Session, Column, ForeignKey, String, UUID, Integer
import uuid
from typing import List
import sqlalchemy.dialects.oracle as ora


ORACLE_DB_USERNAME = "webstore"
ORACLE_DB_PASSWORD = "6GuVk8ADDDawRX2P"
ORACLE_DB_DSN = "(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1521)(host=adb.eu-stockholm-1.oraclecloud.com))(connect_data=(service_name=g9b34ba6c531a5c_olks5kc06813coza_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))"
ORACLE_DB_URL: str = f"oracle+oracledb://{ORACLE_DB_USERNAME}:{ORACLE_DB_PASSWORD}@{ORACLE_DB_DSN}"

engine = create_engine(ORACLE_DB_URL)

class Hero(SQLModel, table=True):
    id: int | None = Field(sa_column=Column(Integer, primary_key=True, default=None))
    name: str = Field(sa_column=Column(String(100), index=True))
    secret_name: str = Field(sa_column=Column(String(100)))
    age: int | None = Field(sa_column=Column(Integer, default=None))


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

create_db_and_tables()

# with Session(engine) as session:
    