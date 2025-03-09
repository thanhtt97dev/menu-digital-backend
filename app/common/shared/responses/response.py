
from typing import Generic, TypeVar, Any

from app.common.shared.constants.app_constant import AppConstants

T = TypeVar('T')
class Response(Generic[T]):
    
    def __init__(self, code, message, data: T | None = None, error: Any | None = None):
        self.code = code
        self.message = message
        if data is not None:
            self.data = data
        if error is not None:
            self.error = error

    @staticmethod
    def success(data: T | None = None, message: str = "Success!"):
        return Response(AppConstants.ResponseCode.SUCCESS, message, data)
    
    @staticmethod    
    def failure(error: Any | None = None, message: str = "Failure!"):
        return Response(AppConstants.ResponseCode.FAILURE, message, None, error)
    
    @staticmethod
    def not_found(error: Any | None = None, data: T | None = None, message: str = "Not Found!"):
        return Response(AppConstants.ResponseCode.NOT_FOUND, message, data, error)
    
    @staticmethod
    def validation_error(error: Any | None = None, message: str = "Validation error!", data: T | None = None):
        return Response(AppConstants.ResponseCode.VALIDATION_ERROR, message, data, error)
    
    @staticmethod
    def un_authorized(error: Any | None = None, message: str = "Un authorized!", data: T | None = None):
        return Response(AppConstants.ResponseCode.UN_AUTHORIZED, message, data, error)
    
    @staticmethod
    def un_authentication(error: Any | None = None, message: str = "Un authentication!", data: T | None = None):
        return Response(AppConstants.ResponseCode.UN_AUTHENTICATION, message, data, error)
    
    @staticmethod
    def initialization(code: str, message: str | None = '', data: T | None = None, error: Any | None = None):
        return Response(code, message, data, error)
