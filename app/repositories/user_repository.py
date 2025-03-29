from sqlalchemy import String, cast, select, or_
from sqlalchemy.orm import Session
from app.models.role import Role
from app.schemas.role_schema import RoleCreate


from app.common.base.base_repository import BaseRepository
from app.models.user import User
class UserRepository(BaseRepository[User]):
    
    def __init__(self, db):
        super().__init__(User,db)
        
    def get_user_by_username(self, username: str) -> User | None:
        query = (
            select(User).where(User.username == username)
        )
        result = self.execute_scalar_one_or_none(query)
        return result
    
    def get_users(self, search: str):
        query = (
            select(
                User.id,
                User.username,
                User.email,
                User.fullname,
                User.status,
                Role.id.label('roleId'),
                Role.name.label("roleName")
            )
            .join(Role, User.role_id == Role.id)
            .where(
                or_(
                    User.fullname.like(f"%{search}%"),
                    User.email.like(f"%{search}%"),
                    cast(User.username, String).like(f"%{search}%")
                )
            )
        )
        return query
    