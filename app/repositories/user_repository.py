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
    
    def get_users(self, username: str = '', fullname: str = '', email: str = '', role_id: int = 0, status: int = -2):
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
                (User.username.contains(username) if username != '' else True),
                User.fullname.contains(fullname),
                User.email.contains(email),
                (User.role_id == role_id if role_id != 0 else True),
                (User.status == status if status != -2 else True)
            )
        )
        return query
    