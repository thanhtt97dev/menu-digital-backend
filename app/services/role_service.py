from sqlalchemy.orm import Session

from app.repositories.role_repository import RoleRepository
from app.schemas.role_schema import RoleCreate, RoleResponse
from app.common.shared.responses.base_response import BaseResponse
from app.common.shared.responses.response import Response
from app.common.shared.exceptions.base.bad_request_exception import BadRequestException

class RoleService:
    
    @staticmethod
    def create_role(db: Session, role_data: RoleCreate) -> RoleResponse:
        is_existed_role = RoleRepository.get_role_by_name(db, role_data.name)
        if is_existed_role:
            raise BadRequestException(title='Role Already Exists', content=f"The role '{role_data.name}' is already taken. Please choose a different name.")
        
        new_role = RoleRepository.create_role(db, role_data)
        data = RoleResponse.from_orm(new_role)
        return Response.success(data=data)
    
    @staticmethod
    def get_all_roles(db: Session):
        data = RoleRepository.get_all_roles(db)
        return Response.success(data)