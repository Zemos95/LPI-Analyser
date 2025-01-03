from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Verbindung zur PostgreSQL-Datenbank
DATABASE_URL = "postgresql://lpi_user:securepassword@localhost:5432/lpi_analyser"

# SQLAlchemy-Engine und Session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Erstellt eine Datenbank-Session und gibt sie zurück.

    Returns:
        Session: Eine neue SQLAlchemy-Datenbank-Session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
