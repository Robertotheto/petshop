from flask import jsonify
from src.use_cases.interfaces.users_authenticate import UsersAuthenticateInterface
from src.use_cases.errors.user_not_found_error import UserNotFoundException
from src.use_cases.errors.user_credentials_error import UserCredentialsException

class UsersAuthenticateController:
    def __init__(self, users_register_use_case: UsersAuthenticateInterface):
        self.__users_register_use_case = users_register_use_case
    def authenticate(self, email: str, password: str) -> dict:
        try:
            return jsonify(self.__users_register_use_case.authenticate(email, password)), 200
        except UserNotFoundException as e:
            return jsonify({"message": str(e)}), 404
        except UserCredentialsException as e:
            return jsonify({"message": str(e)}), 401
       