from abc import ABC, abstractmethod

class UsersRegisterPhotoInterface(ABC):
    @abstractmethod
    def register_photo(self, user_id: str, image: str) -> dict:
        pass
    