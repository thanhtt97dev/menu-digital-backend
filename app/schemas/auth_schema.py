from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class SignIn(BaseModel):
    username: str
    password: str
    
class SignUp(BaseModel):
    username: str = Field(..., min_length=8, max_length=20, description="Username must be between 8 and 20 characters.")
    password: str = Field(..., min_length=8, description="Password must be at least 8 characters long.")
    fullname: str = Field(..., min_length=3, description="Full name must be at least 3 characters long.")
    email: EmailStr = Field(..., description="Invalid email format.")
    
    
class UserModel(BaseModel):
    id: Optional[str] = None
    role: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    
class SignInByGoogle(BaseModel):
    googleToken: str
