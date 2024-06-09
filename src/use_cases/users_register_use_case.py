from datetime import timedelta
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token
from src.repositories.interfaces.users_repository import UsersRepositoryInterface
from src.use_cases.interfaces.users_register import UsersRegisterInterface
from src.use_cases.errors.user_already_exists_error import UserAlreadyExistsException

class UsersRegisterUseCase(UsersRegisterInterface):
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.__users_repository = users_repository

    def register(self, name: str, email: str, password: str) -> dict:
        if self.__users_repository.find_by_email(email):
            raise UserAlreadyExistsException(email)
        password = generate_password_hash(password)
        user = self.__users_repository.create(name, email, password)
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1))
        return formatted_user(user, token)
def formatted_user(user, token)-> dict:
    return {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'token': token,
    }
