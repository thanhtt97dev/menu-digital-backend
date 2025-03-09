import jwt
from datetime import datetime, timedelta

from app.common.abstractions.extenal_services.jwt_service_interface import JwtServiceInterface
from app.common.shared.configurations.enviroment_config import settings
from app.common.shared.exceptions.base.un_authentication_exception import UnAuthenticationException


class JwtService(JwtServiceInterface):
    
    def generate_token(self, payload: dict, secret: str = settings.JWT_ISSUER_SIGNING_KEY, expires_in: int = settings.JWT_EXPIRE_MINUTES, algorithm: str = 'HS256'):
        data = payload.copy()
        expire = datetime.utcnow() + timedelta(minutes=expires_in)
        data.update({"exp": expire})
        return jwt.encode(data, secret, algorithm)
    
    
    def verify_token(self, token: str, secret: str = settings.JWT_ISSUER_SIGNING_KEY, algorithm: str = 'HS256'):
        try:
            payload = jwt.decode(
                token,
                secret,
                algorithms=[algorithm],
                issuer= settings.JWT_VALID_ISSUER if settings.JWT_VALIDATE_ISSUER else None,
                audience= settings.JWT_VALID_AUDIENCE if settings.JWT_VALIDATE_AUDIENCE else None,
                options={"verify_exp": settings.JWT_VALIDATE_LIFETIME},
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise UnAuthenticationException('Un authentication', 'Token exprired!')
        except jwt.InvalidTokenError:
            raise UnAuthenticationException('Un authentication', 'Token invalid!')
        
def get_jwt_service():
    return JwtService()

    