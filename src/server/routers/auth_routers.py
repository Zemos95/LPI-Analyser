from fastapi import APIRouter, HTTPException, Depends
from src.server.auth.auth_manager import authenticate_user

router = APIRouter()

@router.post("/api/login")
async def login(username: str, password: str):
    """
    Login-Endpoint für Benutzer.

    Args:
        username (str): Der Benutzername.
        password (str): Das Passwort.

    Returns:
        dict: Login-Ergebnis.
    """
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Ungültige Anmeldedaten")

    return {"success": True, "message": "Anmeldung erfolgreich", "user": user}
