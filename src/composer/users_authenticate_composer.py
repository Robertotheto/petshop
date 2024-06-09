from src.repositories.user_repository import UsersRepository
from src.use_cases.users_authenticate_use_case import UsersAuthenticateUseCase
from src.controllers.users_authenticate_controller import UsersAuthenticateController

def users_authenticate_composer():
    users_repository = UsersRepository()
    users_authenticate_use_case = UsersAuthenticateUseCase(users_repository)
    return UsersAuthenticateController(users_authenticate_use_case)
