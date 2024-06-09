from src.repositories.pet_repository import PetsRepository
from src.repositories.token_block_list_repository import TokenBlockListRepository
from src.use_cases.get_one_pet_use_case import GetOnePetUseCase
from src.controllers.get_one_pet_controller import GetOnePetController

def get_one_pet_composer():
    pets_repository = PetsRepository()
    token_block_list_repository = TokenBlockListRepository()
    pet_one_use_case = GetOnePetUseCase(pets_repository, token_block_list_repository)
    return GetOnePetController(pet_one_use_case)
