from src.repositories.pet_repository import PetsRepository
from src.repositories.token_block_list_repository import TokenBlockListRepository
from src.use_cases.pet_update_photo_use_case import PetUpdatePhotoUseCase
from src.controllers.pet_update_photo_controller import PetUpdatePhotoController

def pet_update_photo_composer():
    pets_repository = PetsRepository()
    token_block_list_repository = TokenBlockListRepository()
    pet_update_use_case = PetUpdatePhotoUseCase(pets_repository, token_block_list_repository)
    return PetUpdatePhotoController(pet_update_use_case)
