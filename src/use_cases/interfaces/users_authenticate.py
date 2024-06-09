from abc import ABC, abstractmethod

class UsersAuthenticateInterface(ABC):
    @abstractmethod
    def authenticate(self, email: str, password: str) -> dict:
        pass
    