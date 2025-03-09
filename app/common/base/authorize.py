
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer


from app.extenal_services.jwt_service import JwtService, get_jwt_service
from app.common.shared.exceptions.base.un_authorized_exception import UnAuthorizedException
from app.schemas.auth_schema import UserModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def authorize(required_roles: list[str] = None):
    def verify_token(token: str = Depends(oauth2_scheme), jwtService: JwtService = Depends(get_jwt_service)):
        user_data = jwtService.verify_token(token)
        user = UserModel(**user_data)
        if required_roles and user.role not in required_roles:
            raise UnAuthorizedException('Un authorized', 'Access denied')
        return user
    
    return verify_token