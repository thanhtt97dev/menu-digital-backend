
from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer


from app.extenal_services.jwt_service import JwtService, get_jwt_service
from app.common.shared.exceptions.base.un_authorized_exception import UnAuthorizedException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def authorize(required_roles: list[str] = None):
    def verify_token(token: str = Depends(oauth2_scheme), jwtService: JwtService = Depends(get_jwt_service)):
        user = jwtService.verify_token(token)
        if required_roles and user.role not in required_roles:
            raise UnAuthorizedException('Un authorized', 'Access denied')
        return user
    
    return verify_token