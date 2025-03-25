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
    id: str
    username: str | None
    email: str
    fullname: str | None
    role_id: int
    status: int

    class Config:
        from_attributes = True