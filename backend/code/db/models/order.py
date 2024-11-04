from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Order(Base):
    id = Column(Integer, primary_key=True)
    delivery_date = Column(DateTime, nullable=True)
    dispatch_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, nullable=True)

