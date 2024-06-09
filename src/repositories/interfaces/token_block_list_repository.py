from abc import ABC, abstractmethod

class TokenBlockListRepositoryInterface(ABC):
    @abstractmethod
    def insert_jti(self, jti: str) -> None: pass
    
    @abstractmethod
    def compare_jti(self, jti: str) -> bool: pass