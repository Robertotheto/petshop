from src.repositories.user_repository import UsersRepository
from src.repositories.token_block_list_repository import TokenBlockListRepository
from src.use_cases.get_one_users_use_case import GetOneUserUseCase
from src.controllers.get_one_user_controller import GetOneUserController

def get_one_user_composer():
    users_repository = UsersRepository()
    token_block_list_repository = TokenBlockListRepository()
    users_register_use_case = GetOneUserUseCase(users_repository, token_block_list_repository)
    return GetOneUserController(users_register_use_case)
