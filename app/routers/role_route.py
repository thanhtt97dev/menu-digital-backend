from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.role_service import RoleService
from app.schemas.role_schema import  RoleCreate, RoleResponse

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.post("/", response_model= RoleResponse)
def create_role(role_data: RoleCreate, db: Session = Depends(get_db)):
    return RoleService.create_role(db, role_data)
    
@router.get('/')
def get_all_roles(db:Session = Depends(get_db)):
    return RoleService.get_all_roles(db)