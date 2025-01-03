from src.server.database.base import Base
from src.server.database.session import engine, SessionLocal
from src.server.database.model import User

def initialize_database():
    """
    Erstellt die Tabellen in der Datenbank und fügt Testbenutzer hinzu.
    """
    print("Initialisiere die Datenbank...")
    # Tabellen erstellen
    Base.metadata.create_all(bind=engine)
    print("Tabellen erfolgreich erstellt.")

    # Testbenutzer hinzufügen
    db = SessionLocal()
    try:
        # Überprüfen, ob bereits Benutzer existieren
        if db.query(User).first():
            print("Benutzer existieren bereits. Keine neuen Benutzer hinzugefügt.")
            return

        # Benutzer hinzufügen
        admin = User(username="admin", hashed_password=User.hash_password("adminpassword"))
        testuser = User(username="testuser", hashed_password=User.hash_password("testpassword"))
        db.add_all([admin, testuser])
        db.commit()
        print("Benutzer erfolgreich hinzugefügt.")
    except Exception as e:
        db.rollback()
        print(f"Fehler beim Hinzufügen der Benutzer: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    initialize_database()
