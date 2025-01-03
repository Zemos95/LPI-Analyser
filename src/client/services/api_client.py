import requests

def login_request(username: str, password: str) -> dict:
    """
    Führt eine Login-Anfrage an den Server aus.

    Args:
        username (str): Der Benutzername.
        password (str): Das Passwort.

    Returns:
        dict: Die Antwort des Servers.
    """
    url = "http://localhost:8000/api/login"
    payload = {"username": username, "password": password}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Löst eine HTTPError aus bei fehlerhaftem Status
        return response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Serververbindung fehlgeschlagen: {e}")
