from abc import ABC, abstractmethod

class TokenBlockListInterface(ABC):
    @abstractmethod
    def logout(self, jti: str) -> None:
        pass
    