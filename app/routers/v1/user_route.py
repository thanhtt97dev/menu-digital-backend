from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from fastapi_versioning import version

from app.db.database import get_db
from app.services.v1.user_service import UserService
from app.schemas.user_schema import UserCreate, UserResponse
from app.common.shared.constants.app_constant import AppConstants
from app.common.base.authorize import authorize
from app.common.shared.configurations.enviroment_config import enviroment

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("")
@version(enviroment.API_VERSION)
def get_users(
    search: Optional[str] = '' , 
    page_index: int = AppConstants.Page.INDEX_DEFAULT, 
    page_size: int  = AppConstants.Page.SIZE_DEFAULT,
    db: Session = Depends(get_db),
    user = Depends(authorize([AppConstants.Role.Admin]))
):
    return UserService(db).get_users(search, page_index, page_size)