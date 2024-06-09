from abc import ABC, abstractmethod
from src.models.users import Users


class UsersRepositoryInterface(ABC):
    @abstractmethod
    def create(self, name: str, email: str, password: str) -> Users:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Users:
        pass

    @abstractmethod
    def find_by_id(self, user_id: str) -> Users:
        pass

    @abstractmethod
    def insert_photo(self,user_id:str, image_url: str) -> Users:
        pass
    
    @abstractmethod
    def get_one_user(self, user_id: str) -> Users:
        pass