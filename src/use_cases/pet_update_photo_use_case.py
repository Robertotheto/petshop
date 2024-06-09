from flask_jwt_extended import get_jwt
from src.repositories.interfaces.pets_repository import PetsRepositoryInterface
from src.use_cases.interfaces.pet_update_photo import PetUpdatePhotoInterface
from src.repositories.interfaces.token_block_list_repository import TokenBlockListRepositoryInterface
from src.use_cases.errors.user_not_found_error import UserNotFoundException
from src.use_cases.errors.user_unauthorized_error import UserUnauthorizedError

class PetUpdatePhotoUseCase(PetUpdatePhotoInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface, token_block_list_repository: TokenBlockListRepositoryInterface):
        self.__pets_repository = pets_repository
        self.__token_block_list_repository = token_block_list_repository

    def pet_update_photo(self, pet_id: str, image: str) -> dict:
        jti = get_jwt()['jti']
        if self.__token_block_list_repository.compare_jti(jti):
            raise UserUnauthorizedError()
        pet = self.__pets_repository.find_by_id(pet_id)
        if not pet:
            raise UserNotFoundException()

        updated_photo = self.__pets_repository.update_photo_pet(pet_id,image)

        return formatted_pet(updated_photo)
def formatted_pet(pet)-> dict:
    return {
        'id': pet.id,
        'name': pet.name,
        'race': pet.race,
        'age': pet.age,
        'image': pet.image,
        'user_id': pet.user_id,
    }
