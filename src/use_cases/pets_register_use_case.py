from src.repositories.interfaces.pets_repository import PetsRepositoryInterface
from src.use_cases.interfaces.pets_register import PetsRegisterInterface
from src.repositories.interfaces.users_repository import UsersRepositoryInterface
from src.use_cases.errors.user_not_found_error import UserNotFoundException

class PetsRegisterUseCase(PetsRegisterInterface):
    def __init__(self, users_repository: UsersRepositoryInterface, pets_repository: PetsRepositoryInterface):
        self.__users_repository = users_repository
        self.__pets_repository = pets_repository

    def register(self, name: str, race: str, age: str, user_id: str) -> dict:
        user = self.__users_repository.find_by_id(user_id)
        if not user:
            raise UserNotFoundException()
        pet = self.__pets_repository.create(name,race,age,user.id)
        return formatted_pet(pet)
def formatted_pet(pet)-> dict:
    return {
        'id': pet.id,
        'name': pet.name,
        'race': pet.race,
        'age': pet.age,
        'user_id': pet.user_id
    }
