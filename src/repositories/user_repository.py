from src.database.settings import db
from src.models.users import Users
from src.repositories.interfaces.users_repository import UsersRepositoryInterface


class UsersRepository(UsersRepositoryInterface):
    def create(self, name: str, email: str, password: str) -> Users:
        try:
            user = Users(name=name, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            db.session.refresh(user)
            return user
        except Exception as exception:
            db.session.rollback()
            raise exception
    def find_by_email(self, email: str) -> Users:
        try:
            return db.session.query(Users).filter(Users.email == email).first()
        except Exception as exception:
            raise exception
    def find_by_id(self, user_id: str) -> Users:
        try:
            return db.session.query(Users).filter(Users.id == user_id).first()
        except Exception as exception:
            raise exception
    def insert_photo(self,user_id:str, image_url: str) -> Users:
        try:
            user = db.session.query(Users).filter(Users.id == user_id).first()
            user.image = image_url
            db.session.commit()
            db.session.refresh(user)
            return user
        except Exception as exception:
            db.session.rollback()
            raise exception
    def get_one_user(self, user_id: str) -> Users:
        try:
            user = db.session.query(Users).filter(Users.id == user_id).first()
            return user
        except Exception as exception:
            raise exception