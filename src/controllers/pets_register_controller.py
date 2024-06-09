from flask import jsonify
from src.use_cases.interfaces.pets_register import PetsRegisterInterface
from src.use_cases.errors.user_not_found_error import UserNotFoundException

class PetsRegisterController:
    def __init__(self, pets_register_use_case: PetsRegisterInterface):
        self.__pets_register_use_case = pets_register_use_case
    def register(self, name,race,age,user_id) -> dict:
        try:
            return jsonify(self.__pets_register_use_case.register(name, race, age, user_id)), 201
        except UserNotFoundException as e:
            return jsonify({"message": str(e)}), 404
       