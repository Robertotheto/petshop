from datetime import timedelta
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from src.repositories.interfaces.users_repository import UsersRepositoryInterface
from src.use_cases.interfaces.users_authenticate import UsersAuthenticateInterface
from src.use_cases.errors.user_not_found_error import UserNotFoundException
from src.use_cases.errors.user_credentials_error import UserCredentialsException

class UsersAuthenticateUseCase(UsersAuthenticateInterface):
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.__users_repository = users_repository

    def authenticate(self, email: str, password: str) -> dict:
        user = self.__users_repository.find_by_email(email)
        if user is None:
            raise UserNotFoundException()
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1))
        if user and check_password_hash(user.password, password):
            return formatted_user(user, token)
        raise UserCredentialsException()
def formatted_user(user, token)-> dict:
    return {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'token': token,
    }
