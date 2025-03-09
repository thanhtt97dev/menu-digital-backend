from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class UserShop(Base):

    __tablename__ = "user_shop"

    user_id = Column(String(36), ForeignKey("user.id"), primary_key=True)
    shop_id = Column(String(36), ForeignKey("shop.id"), primary_key=True)
    date_created = Column(DateTime)

    user = relationship("User", back_populates="user_shops")
    shop = relationship("Shop", back_populates="user_shops")