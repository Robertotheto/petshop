from src.repositories.token_block_list_repository import TokenBlockListRepository
from src.use_cases.users_logout_use_case import UserLogoutUseCase
from src.controllers.users_logout_controller import UserLogoutController

def users_logout_composer():
    token_block_list_repository = TokenBlockListRepository()
    user_logout_use_case = UserLogoutUseCase(token_block_list_repository)
    return UserLogoutController(user_logout_use_case)
