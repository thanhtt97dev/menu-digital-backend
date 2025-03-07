from app.common.shared.exceptions.base.domain_exception import DomainException

class NotFoundException(DomainException):

    def __init__(self, title, content):
        super().__init__(title, content)
        self.title = title,
        self.content = content