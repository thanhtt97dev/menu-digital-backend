from abc import ABC, abstractmethod

class JwtServiceInterface(ABC):
    
    @abstractmethod
    def generate_token(self, palyload: dict, expires_in: int, secret: str, algorithm: str):
        pass
    
    @abstractmethod
    def verify_token(self, token: str, secret: str, algorithm: str):
        pass