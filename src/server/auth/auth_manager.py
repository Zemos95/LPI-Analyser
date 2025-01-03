from typing import Optional
from src.server.models.user_model import User
from src.server.database import get_db

def authenticate_user(username: str, password: str) -> Optional[dict]:
    """
    Prüft, ob der Benutzer berechtigt ist, sich anzumelden.

    Args:
        username (str): Der Benutzername.
        password (str): Das Passwort.

    Returns:
        dict | None: Benutzerinformationen, falls gültig.
    """
    db = get_db()
    user = db.query(User).filter_by(username=username).first()
    if user and user.verify_password(password):  # Angenommen, die Methode ist implementiert
        return {"id": user.id, "username": user.username}
    return None
