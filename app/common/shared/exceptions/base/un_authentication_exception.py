from app.common.shared.exceptions.base.domain_exception import DomainException

class UnAuthenticationException(DomainException):

    def __init__(self, title, message):
        super().__init__(title, message)
        self.title = title,
        self.message = message