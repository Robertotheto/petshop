import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from src.database.settings import db

class TokenBlockList(db.Model):
    __tablename__ = 'token_block_list'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    jti = Column(String, nullable=False)

def __repr__(self):
    return f'<Token {self.id}>'