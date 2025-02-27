from sqlalchemy.orm import Session
from app.repositories.role_repository import RoleRepository
from app.schemas.role import RoleCreate, RoleResponse

class RoleService:
    
    @staticmethod
    def create_role(db: Session, role_data: RoleCreate) -> RoleResponse:
        is_existed_role = RoleRepository.get_role_by_name(db, role_data.name)
        if is_existed_role:
            raise ValueError("Role already exists")
        
        new_role = RoleRepository.create_role(db, role_data)
        return RoleResponse.from_orm(new_role)
    
    @staticmethod
    def get_all_roles(db: Session):
        return RoleRepository.get_all_roles(db)