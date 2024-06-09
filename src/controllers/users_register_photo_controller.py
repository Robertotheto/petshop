from flask import jsonify
from src.use_cases.interfaces.user_register_photo import UsersRegisterPhotoInterface
from src.use_cases.errors.user_not_found_error import  UserNotFoundException
from src.use_cases.errors.user_unauthorized_error import UserUnauthorizedError

class UsersRegisterPhotoController:
    def __init__(self, users_register_use_case: UsersRegisterPhotoInterface):
        self.__users_register_use_case = users_register_use_case
    def register_photo(self, user_id: str, image: str) -> dict:
        try:
            return jsonify(self.__users_register_use_case.register_photo(user_id, image)), 200
        except UserUnauthorizedError as e:
            return jsonify({"message": str(e)}), 401
        except UserNotFoundException as e:
            return jsonify({"message": str(e)}), 404
       