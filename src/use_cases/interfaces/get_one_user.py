from abc import ABC, abstractmethod

class GetOneUserInterface(ABC):
    @abstractmethod
    def get_user(self, user_id: str) -> dict:
        pass
    