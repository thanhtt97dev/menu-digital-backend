from fastapi import APIRouter, Depends
from fastapi_versioning import version
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.v1.role_service import RoleService
from app.schemas.role_schema import  RoleCreate, RoleResponse
from app.common.base.authorize import authorize
from app.common.shared.constants.app_constant import AppConstants
from app.common.shared.configurations.enviroment_config import enviroment

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.post("", response_model= RoleResponse)
@version(enviroment.API_VERSION)
def create_role(role_data: RoleCreate, db: Session = Depends(get_db), user = Depends(authorize([AppConstants.Role.Admin]))):
    return RoleService.create_role(db, role_data)
    
@router.get('')
@version(enviroment.API_VERSION)
def get_all_roles(db:Session = Depends(get_db)):
    return RoleService.get_all_roles(db)