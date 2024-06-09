from abc import ABC, abstractmethod

class PetsRegisterInterface(ABC):
    @abstractmethod
    def register(self, name: str, race: str, age: str, user_id: str) -> dict:
        pass
    