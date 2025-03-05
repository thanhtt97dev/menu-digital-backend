
class DomainException(Exception):

    def __init__(self, title, message):
        super().__init__(message)
        self.title = title
        self.message = message