from pydantic import BaseModel

class RoleCreate(BaseModel):
    name: str
    
class RoleResponse(BaseModel):
    id: int
    name: str
    
    class Config:
        rom_attributes = True  # Allows SQLAlchemy to Pydantic conversion