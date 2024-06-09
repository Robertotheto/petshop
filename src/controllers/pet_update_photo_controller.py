from flask import jsonify
from src.use_cases.interfaces.pet_update_photo import PetUpdatePhotoInterface
from src.use_cases.errors.user_not_found_error import  UserNotFoundException
from src.use_cases.errors.user_unauthorized_error import UserUnauthorizedError

class PetUpdatePhotoController:
    def __init__(self, pets_update_use_case: PetUpdatePhotoInterface):
        self.__pets_update_use_case = pets_update_use_case
    def  pet_update_photo(self, pet_id: str, image: str) -> dict:
        try:
            return jsonify(self.__pets_update_use_case.pet_update_photo(pet_id, image)), 200
        except UserUnauthorizedError as e:
            return jsonify({"message": str(e)}), 401
        except UserNotFoundException as e:
            return jsonify({"message": str(e)}), 404
       