from flask import jsonify
from src.use_cases.interfaces.users_logout import TokenBlockListInterface
from src.use_cases.errors.user_unauthorized_error import UserUnauthorizedError

class UserLogoutController:
    def __init__(self, user_logout_use_case: TokenBlockListInterface):
        self.__user_logout_use_case = user_logout_use_case

    def logout(self, jti: str) -> dict:
        try:
            self.__user_logout_use_case.logout(jti)
            return jsonify({"message": "Logout successfully"}), 200
        except UserUnauthorizedError as e:
            return jsonify({"message": str(e)}), 401
        