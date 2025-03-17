from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    
    __tablename__ = "user"
    
    id = Column(String(36), primary_key=True, unique=True, nullable=False)
    role_id = Column(Integer, ForeignKey("role.id"))
    username = Column(String(50), unique=True, nullable=True)
    password = Column(String(255), nullable=True)
    fullname = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    status = Column(Integer, nullable=False)
    
    role = relationship("Role", back_populates="users")
    user_shops = relationship("UserShop", back_populates="user")
