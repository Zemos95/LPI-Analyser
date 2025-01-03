from sqlalchemy import Column, Integer, String
from .base import Base
import bcrypt

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    def verify_password(self, password: str) -> bool:
        """
        Überprüft das Passwort mit dem gespeicherten Hash.
        """
        return bcrypt.checkpw(password.encode('utf-8'), self.hashed_password.encode('utf-8'))

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hashing des Passworts für die Speicherung.
        """
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
