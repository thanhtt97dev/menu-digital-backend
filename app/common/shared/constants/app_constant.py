from dataclasses import dataclass

@dataclass(frozen=True)
class AppConstants:

    @dataclass(frozen=True)
    class Page:
        INDEX_DEFAULT: int = 1
        SIZE_DEFAULT: int = 10
        

    @dataclass(frozen=True)
    class ResponseCode:
        SUCCESS: str = '0000'
        FAILURE: str = '0001'
        NOT_FOUND: str = '0002'
        VALIDATION_ERROR: str = '0003'
        UN_AUTHORIZED: str = '0004'
        UN_AUTHENTICATION: str = '0005'
        
    @dataclass(frozen=True)
    class User:
        @dataclass(frozen=True)
        class Status:
            UnActivate = -1
            Deactivate = 0
            Activate = 1
            
    @dataclass(frozen=True)
    class Role:
       Admin = 1
       Shop_Admin = 2
       Employee = 3
       Customer = 4

