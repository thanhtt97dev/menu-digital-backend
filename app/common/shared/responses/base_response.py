from app.common.shared.constants.app_constant import AppConstants

class BaseResponse:

    def __init__(self, code: str, message: str | None):
        self.code = code
        self.message = message

    @staticmethod
    def success(message: str = "Success!"):
        return BaseResponse(AppConstants.ResponseCode.SUCCESS, message)
    
    @staticmethod    
    def failure(message: str = "Failure!"):
        return BaseResponse(AppConstants.ResponseCode.FAILURE, message)
    
    @staticmethod
    def not_found(message: str = "Not Found!"):
        return BaseResponse(AppConstants.ResponseCode.NOT_FOUND, message)

    @staticmethod
    def validation_error(message: str = "Validation error!"):
        return BaseResponse(AppConstants.ResponseCode.VALIDATION_ERROR, message)
    
    @staticmethod
    def un_authorized(message: str = "Un authorized!"):
        return BaseResponse(AppConstants.ResponseCode.UN_AUTHORIZED, message)
    
    @staticmethod
    def un_authentication(message: str = "Un authentication!"):
        return BaseResponse(AppConstants.ResponseCode.UN_AUTHENTICATION, message)
    
    @staticmethod
    def initialization(code: str, message: str | None):
        return BaseResponse(code, message)
