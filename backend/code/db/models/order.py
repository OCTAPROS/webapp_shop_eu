from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey, Identity
from sqlalchemy.orm import relationship

from db.base_class import Base


class Order(Base):
    id_identity = Identity(start=1, increment=1)
    id = Column(Integer, id_identity, primary_key=True)
    delivery_date = Column(DateTime, nullable=True)
    dispatch_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, nullable=True)

