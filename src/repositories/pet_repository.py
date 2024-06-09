from src.database.settings import db
from src.models.pets import Pets
from src.repositories.interfaces.pets_repository import PetsRepositoryInterface

class PetsRepository(PetsRepositoryInterface):
    def create(self, name: str, race: str, age: str, user_id: str) -> Pets:
        try:
            pet = Pets(name=name,race=race,age=age,user_id=user_id)
            db.session.add(pet)
            db.session.commit()
            db.session.refresh(pet)
            return pet
        except Exception as exception:
            db.session.rollback()
            raise exception
    def find_by_id(self, pet_id: str) -> Pets:
        try:
            return db.session.query(Pets).filter(Pets.id == pet_id).first()
        except Exception as exception:
            raise exception
    def update_photo_pet(self, pet_id: str, image_url: str) -> Pets:
        try:
            pet = db.session.query(Pets).filter(Pets.id == pet_id).first()
            pet.image = image_url
            db.session.commit()
            db.session.refresh(pet)
            return pet
        except Exception as exception:
            db.session.rollback()
            raise exception
    def get_one_pet(self, pet_id: str) -> Pets:
        try:
            return db.session.query(Pets).filter(Pets.id == pet_id).first()
        except Exception as exception:
            raise exception
        