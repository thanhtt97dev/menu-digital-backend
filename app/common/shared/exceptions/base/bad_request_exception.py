from app.common.shared.exceptions.base.domain_exception import DomainException

class BadRequestException(DomainException):
    def __init__(self, message):
        super().__init__(message)
        self.message = message