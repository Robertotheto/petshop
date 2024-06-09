from flask import jsonify
from src.use_cases.interfaces.get_one_pet import GetOnePetInterface
from src.use_cases.errors.user_not_found_error import  UserNotFoundException
from src.use_cases.errors.user_unauthorized_error import UserUnauthorizedError

class GetOnePetController:
    def __init__(self, pet_one_use_case: GetOnePetInterface):
        self.__pet_one_use_case = pet_one_use_case
    def get_pet(self, pet_id: str) -> dict:
        try:
            return jsonify(self.__pet_one_use_case.get_pet(pet_id)), 200
        except UserUnauthorizedError as e:
            return jsonify({"message": str(e)}), 401
        except UserNotFoundException as e:
            return jsonify({"message": str(e)}), 404
       