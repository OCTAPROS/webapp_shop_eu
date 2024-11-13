from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey, Double, Identity, Numeric
from sqlalchemy.orm import relationship

from db.base_class import Base


class Product(Base):
    id_identity = Identity(start=1, increment=1)
    id = Column(Integer, id_identity, primary_key=True)
    name = Column(String(100), nullable=False)
    image_uri = Column(String(500), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Numeric(10, 4), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, nullable=True)