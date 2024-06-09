from src.repositories.user_repository import UsersRepository
from src.use_cases.users_register_use_case import UsersRegisterUseCase
from src.controllers.users_register_controller import UsersRegisterController

def users_register_composer():
    users_repository = UsersRepository()
    users_register_use_case = UsersRegisterUseCase(users_repository)
    return UsersRegisterController(users_register_use_case)
