from src.repositories.interfaces.token_block_list_repository import (
    TokenBlockListRepositoryInterface)
from src.use_cases.interfaces.users_logout import TokenBlockListInterface
from src.use_cases.errors.user_unauthorized_error import UserUnauthorizedError


class UserLogoutUseCase(TokenBlockListInterface):
    def __init__(self, token_block_list_repository: TokenBlockListRepositoryInterface):
        self.__token_block_list_repository = token_block_list_repository

    def logout(self, jti: str) -> None:
        if jti:
            self.__token_block_list_repository.insert_jti(jti)
        else:
            raise UserUnauthorizedError()
