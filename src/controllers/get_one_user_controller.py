from flask import jsonify
from src.use_cases.interfaces.get_one_user import GetOneUserInterface
from src.use_cases.errors.user_not_found_error import  UserNotFoundException
from src.use_cases.errors.user_unauthorized_error import UserUnauthorizedError

class GetOneUserController:
    def __init__(self, users_register_use_case: GetOneUserInterface):
        self.__users_register_use_case = users_register_use_case
    def get_user(self, user_id: str) -> dict:
        try:
            return jsonify(self.__users_register_use_case.get_user(user_id)), 200
        except UserUnauthorizedError as e:
            return jsonify({"message": str(e)}), 401
        except UserNotFoundException as e:
            return jsonify({"message": str(e)}), 404
       