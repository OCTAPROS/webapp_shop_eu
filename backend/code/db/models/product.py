from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey, Double
from sqlalchemy.orm import relationship

from db.base_class import Base


class Product(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    image_uri = Column(String(500), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Double, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, nullable=True)