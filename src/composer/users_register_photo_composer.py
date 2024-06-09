from src.repositories.user_repository import UsersRepository
from src.repositories.token_block_list_repository import TokenBlockListRepository
from src.use_cases.users_register_photo_use_case import UsersRegisterPhotoUseCase
from src.controllers.users_register_photo_controller import UsersRegisterPhotoController

def users_register_photo_composer():
    users_repository = UsersRepository()
    token_block_list_repository = TokenBlockListRepository()
    users_register_use_case = UsersRegisterPhotoUseCase(users_repository, token_block_list_repository)
    return UsersRegisterPhotoController(users_register_use_case)
