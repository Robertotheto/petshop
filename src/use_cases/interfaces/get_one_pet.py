from abc import ABC, abstractmethod

class GetOnePetInterface(ABC):
    @abstractmethod
    def get_pet(self, pet_id: str) -> dict:
        pass
    