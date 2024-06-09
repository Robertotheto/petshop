from flask import jsonify
from src.use_cases.interfaces.users_register import UsersRegisterInterface
from src.use_cases.errors.user_already_exists_error import UserAlreadyExistsException

class UsersRegisterController:
    def __init__(self, users_register_use_case: UsersRegisterInterface):
        self.__users_register_use_case = users_register_use_case
    def register(self, name: str, email: str, password: str) -> dict:
        try:
            return jsonify(self.__users_register_use_case.register(name, email, password)), 201
        except UserAlreadyExistsException as e:
            return jsonify({"message": str(e)}), 409
       