class DomainException(Exception):
    def __init__(self, title: str, content: str):
        super().__init__(content)
        self.title = title
        self.content = content