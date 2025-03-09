from abc import ABC, abstractmethod
from typing import Union, List

class MailServiceInterface(ABC):
    
    @abstractmethod
    def send_mail(self, emails: Union[str, List[str]], subject: str, content: str):
        pass
