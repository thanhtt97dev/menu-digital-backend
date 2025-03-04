from typing import Generic, TypeVar, Type, Tuple, Any

from app.common.shared.constants.app_constant import AppConstants

class BaseResponse:

    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message

    @staticmethod
    def success():
        return BaseResponse(AppConstants.ResponseCode.SUCCESS, "Success!")
    
    @staticmethod    
    def failure():
        return BaseResponse(AppConstants.ResponseCode.FAILURE, "Failure!")
    
    @staticmethod
    def not_found():
        return BaseResponse(AppConstants.ResponseCode.NOT_FOUND, "Not Found!")
    
    @staticmethod
    def validation_error():
        return BaseResponse(AppConstants.ResponseCode.VALIDATION_ERROR, "Validation error!")
    
    @staticmethod
    def un_authorized():
        return BaseResponse(AppConstants.ResponseCode.UN_AUTHORIZED, "Un authorized!")
    
    @staticmethod
    def un_authentication():
        return BaseResponse(AppConstants.ResponseCode.UN_AUTHENTICATION, "Un authentication!")
