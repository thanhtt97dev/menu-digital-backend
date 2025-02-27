from sqlalchemy.orm import Session
from app.models.role import Role
from app.schemas.role import RoleCreate

class RoleRepository:
    @staticmethod
    def create_role(db: Session, role_data: RoleCreate) -> Role:
        db_role = Role(**role_data.dict())
        db.add(db_role)
        db.commit()
        db.refresh(db_role)
        return db_role
    
    @staticmethod
    def get_role_by_name(db: Session, name: str):
        return db.query(Role).filter(Role.name == name).first()
    
    @staticmethod
    def get_all_roles(db: Session):
        return db.query(Role).all()