from flask_jwt_extended import get_jwt
from src.repositories.interfaces.users_repository import UsersRepositoryInterface
from src.use_cases.interfaces.get_one_user import GetOneUserInterface
from src.repositories.interfaces.token_block_list_repository import TokenBlockListRepositoryInterface
from src.use_cases.errors.user_not_found_error import UserNotFoundException
from src.use_cases.errors.user_unauthorized_error import UserUnauthorizedError

class GetOneUserUseCase(GetOneUserInterface):
    def __init__(self, users_repository: UsersRepositoryInterface, token_block_list_repository: TokenBlockListRepositoryInterface):
        self.__users_repository = users_repository
        self.__token_block_list_repository = token_block_list_repository

    def get_user(self, user_id: str) -> dict:
        jti = get_jwt()['jti']
        if self.__token_block_list_repository.compare_jti(jti):
            raise UserUnauthorizedError()
        user = self.__users_repository.get_one_user(user_id)
        if user is None:
            raise UserNotFoundException()
        return formatted_user(user)
def formatted_user(user)-> dict:
    return {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'image': user.image,
    }
