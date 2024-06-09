from abc import ABC, abstractmethod

class UsersRegisterInterface(ABC):
    @abstractmethod
    def register(self, name: str, email: str, password: str) -> dict:
        pass
    