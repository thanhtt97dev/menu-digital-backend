from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import relationship
from app.db.database import Base

class Shop(Base):

    __tablename__ = "shop"

    id = Column(String(36), primary_key=True, unique=True, nullable=False)
    shop_name = Column(String(200), nullable=False)
    address  = Column(Text, nullable=False)
    phone = Column(String(20), nullable=True)
    logo = Column(Text, nullable=True)
    status = Column(Integer, nullable=False)

    user_shops = relationship("UserShop", back_populates="shop")