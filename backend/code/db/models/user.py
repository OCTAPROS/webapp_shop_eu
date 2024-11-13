from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey, Identity
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    id_identity = Identity(start=1, increment=1)
    id = Column(Integer, id_identity, primary_key=True)
    email = Column(String(100), nullable=False, unique=True, index=True)
    password = Column(String(100), nullable=False)
    is_superuser = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, nullable=True)

