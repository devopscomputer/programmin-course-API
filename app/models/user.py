from sqlalchemy import Column, Integer, String
from app.database.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)  # Usando apenas String para email
    full_name = Column(String(100))
    hashed_password = Column(String(128))