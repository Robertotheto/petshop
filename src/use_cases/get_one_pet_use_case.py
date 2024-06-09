from flask_jwt_extended import get_jwt
from src.repositories.interfaces.pets_repository import PetsRepositoryInterface
from src.use_cases.interfaces.get_one_pet import GetOnePetInterface
from src.repositories.interfaces.token_block_list_repository import TokenBlockListRepositoryInterface
from src.use_cases.errors.user_not_found_error import UserNotFoundException
from src.use_cases.errors.user_unauthorized_error import UserUnauthorizedError

class GetOnePetUseCase(GetOnePetInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface, token_block_list_repository: TokenBlockListRepositoryInterface):
        self.__pets_repository = pets_repository
        self.__token_block_list_repository = token_block_list_repository

    def get_pet(self, pet_id: str) -> dict:
        jti = get_jwt()['jti']
        if self.__token_block_list_repository.compare_jti(jti):
            raise UserUnauthorizedError()
        pet = self.__pets_repository.get_one_pet(pet_id)
        if pet_id is None:
            raise UserNotFoundException()
        return formatted_pet(pet)
def formatted_pet(pet)-> dict:
    return {
        'id': pet.id,
        'name': pet.name,
        'race': pet.race,
        'age': pet.age,
        'image': pet.image
    }
