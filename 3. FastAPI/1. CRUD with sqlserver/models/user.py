from sqlalchemy import Column, Integer, String, Boolean, DateTime
from models.database import Base


class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    roleId = Column(Integer)
    Email = Column(String)
    Status = Column(Boolean)
    FullName = Column(String)
    CreateDate = Column(DateTime)
    ModifiledDate = Column(DateTime)
    CoverPhoto = Column(String)