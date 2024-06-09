from src.models.token_block_list import TokenBlockList
from src.database.settings import db
from src.repositories.interfaces.token_block_list_repository import TokenBlockListRepositoryInterface

class TokenBlockListRepository(TokenBlockListRepositoryInterface):
    def insert_jti(self, jti: str) -> None:
        try:
            token_block_list = TokenBlockList(jti=jti)
            db.session.add(token_block_list)
            db.session.commit()
        except Exception as exception:
            db.session.rollback()
            raise exception

    def compare_jti(self, jti: str) -> bool:
        try:
            return bool(db.session.query(TokenBlockList).filter(TokenBlockList.jti == jti).first())
        except Exception as exception:
            raise exception