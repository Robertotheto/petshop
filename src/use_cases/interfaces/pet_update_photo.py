from abc import ABC, abstractmethod

class PetUpdatePhotoInterface(ABC):
    @abstractmethod
    def pet_update_photo(self, pet_id: str, image: str) -> dict:
        pass
    