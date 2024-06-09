import uuid
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from src.database.settings import db

class Pets(db.Model):
    __tablename__ = 'pets'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    race = Column(String, nullable=False)
    age = Column(String, nullable=False)
    image = Column(String, nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=True)

def __repr__(self):
    return f'<User {self.name}>'
