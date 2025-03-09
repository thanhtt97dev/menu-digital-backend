from app.common.shared.exceptions.base.domain_exception import DomainException

class BadRequestException(DomainException):
    def __init__(self, title, content):
        super().__init__(title, content)
        if title is not None:
            self.title = title
        self.content = content