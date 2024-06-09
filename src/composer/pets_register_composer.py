from src.repositories.user_repository import UsersRepository
from src.repositories.pet_repository import PetsRepository
from src.use_cases.pets_register_use_case import PetsRegisterUseCase
from src.controllers.pets_register_controller import PetsRegisterController

def pets_register_composer():
    users_repository = UsersRepository()
    pets_repository = PetsRepository()
    pets_register_use_case = PetsRegisterUseCase(users_repository, pets_repository)
    return PetsRegisterController(pets_register_use_case)
