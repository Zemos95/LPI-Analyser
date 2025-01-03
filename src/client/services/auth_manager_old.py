import requests
import logging
from src.client.config.settings import BASE_URL


def authenticate_user(username: str, password: str, logger: logging.Logger) -> requests.Response:
    """
    Sendet die Anmeldedaten an den Server und gibt die Antwort zurück.

    Args:
        username (str): Benutzername.
        password (str): Passwort.
        logger (logging.Logger): Der Logger für das Protokollieren von Ereignissen.

    Returns:
        requests.Response: Das Antwortobjekt des Servers.

    Raises:
        ConnectionError: Wenn ein Netzwerkfehler auftritt.
        HTTPError: Wenn der Server einen Fehlerstatus zurückgibt.
    """
    try:
        logger.info(f"Versuche Anmeldung für Benutzer: {username}")
        
        # Anfrage an den Server senden
        response = requests.post(
            f"{BASE_URL}/login",
            json={"username": username, "password": password}
        )
        
        # Logge den Statuscode
        logger.info(f"Antwort vom Server erhalten: {response.status_code} {response.reason}")

        # Falls ein HTTP-Fehlerstatus auftritt, wird eine Exception ausgelöst
        response.raise_for_status()

        logger.info("Anfrage erfolgreich verarbeitet.")
        return response

    except requests.HTTPError as http_err:
        logger.error(f"HTTP-Fehler bei der Anmeldung von {username}: {http_err}")
        raise

    except requests.RequestException as req_err:
        logger.error(f"Netzwerkfehler bei der Anmeldung von {username}: {req_err}")
        raise ConnectionError(f"Netzwerkfehler: {req_err}")
