from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username:str
    email: EmailStr
    
class UserCreate(UserBase):
    password: str
    
class UserResponse(UserBase):
    id:int
    
class Config:
    from_attribute = True    
    
class UserSchema(BaseModel):
    id: Optional[str]
    username: Optional[str]
    email: Optional[str]
    fullname: Optional[str]
    status: Optional[int]
    roleId: Optional[int]
    roleName: Optional[str]

    class Config:
        from_attributes = True
        
class UserUpdateStatus(BaseModel):
    status: int = 1