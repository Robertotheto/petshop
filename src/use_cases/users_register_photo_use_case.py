from flask_jwt_extended import get_jwt
from src.repositories.interfaces.users_repository import UsersRepositoryInterface
from src.use_cases.interfaces.user_register_photo import UsersRegisterPhotoInterface
from src.repositories.interfaces.token_block_list_repository import TokenBlockListRepositoryInterface
from src.use_cases.errors.user_not_found_error import UserNotFoundException
from src.use_cases.errors.user_unauthorized_error import UserUnauthorizedError

class UsersRegisterPhotoUseCase(UsersRegisterPhotoInterface):
    def __init__(self, users_repository: UsersRepositoryInterface, token_block_list_repository: TokenBlockListRepositoryInterface):
        self.__users_repository = users_repository
        self.__token_block_list_repository = token_block_list_repository

    def register_photo(self, user_id: str, image: str) -> dict:
        jti = get_jwt()['jti']
        if self.__token_block_list_repository.compare_jti(jti):
            raise UserUnauthorizedError()
        user = self.__users_repository.find_by_id(user_id)
        if not user:
            raise UserNotFoundException()

        updated_photo = self.__users_repository.insert_photo(user_id,image)

        return formatted_user(updated_photo)
def formatted_user(user)-> dict:
    return {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'image': user.image,
    }
