from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from fastapi_versioning import version

from app.db.database import get_db
from app.services.v1.user_service import UserService
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdateStatus
from app.common.shared.constants.app_constant import AppConstants
from app.common.base.authorize import authorize
from app.common.shared.configurations.enviroment_config import enviroment

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("")
@version(enviroment.API_VERSION)
def get_users(
    username: Optional[str] = '' , 
    fullname: Optional[str] = '' , 
    email: Optional[str] = '' , 
    roleId: Optional[int] = 0,
    statusId: Optional[int] = 0,
    pageIndex: Optional[int] = AppConstants.Page.INDEX_DEFAULT, 
    pageSize: Optional[int]  = AppConstants.Page.SIZE_DEFAULT,
    db: Session = Depends(get_db),
    user = Depends(authorize([AppConstants.Role.Admin]))
):
    return UserService(db).get_users(username, fullname, email, roleId, statusId, pageIndex, pageSize)

@router.put("/status/{id}")
@version(enviroment.API_VERSION)
def update_user_status(
    id: str,
    user_update: UserUpdateStatus,
    db: Session = Depends(get_db),
    user = Depends(authorize([AppConstants.Role.Admin]))
):
    return UserService(db).update_user_status(id, user_update)