from abc import ABC, abstractmethod
from src.models.pets import Pets


class PetsRepositoryInterface(ABC):
    @abstractmethod
    def create(self, name: str, race: str, age: str, user_id: str) -> Pets:
        pass
    @abstractmethod
    def find_by_id(self, pet_id: str) -> Pets:
        pass
    @abstractmethod
    def update_photo_pet(self,pet_id:str, image_url: str) -> Pets:
        pass
    @abstractmethod
    def get_one_pet(self,pet_id: str) -> Pets:
        pass
