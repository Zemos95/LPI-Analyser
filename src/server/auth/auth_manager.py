from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.server.auth.auth_manager import authenticate_user
from src.server.database.session import get_db

router = APIRouter()

@router.post("/api/login")
async def login(username: str, password: str, db: Session = Depends(get_db)):
    """
    Login-Endpunkt für Benutzer.

    Args:
        username (str): Der Benutzername.
        password (str): Das Passwort.
        db (Session): Datenbank-Session.

    Returns:
        dict: Ergebnis der Authentifizierung.
    """
    user = authenticate_user(username, password, db)
    if not user:
        raise HTTPException(status_code=401, detail="Ungültige Anmeldedaten")

    return {"success": True, "message": "Anmeldung erfolgreich", "user": user}
