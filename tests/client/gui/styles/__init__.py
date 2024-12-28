import os
import sys
from src.utils.logging_setup import Logger  # Dein Logger
from PyQt6.QtWidgets import QApplication
from src.utils.logging_setup import Logger  # Importiere den Logger

logger = Logger().get_logger()  # Logger abrufen

def apply_stylesheet(app: QApplication, stylesheet_name: str) -> None:
    """
    Lädt und wendet ein Stylesheet (QSS-Datei) auf die Anwendung an.

    Args:
        app (QApplication): Die PyQt-Anwendung.
        stylesheet_name (str): Der Name der Stylesheet-Datei im Verzeichnis `styles`.

    Raises:
        FileNotFoundError: Wenn die Stylesheet-Datei nicht gefunden wird.
        ValueError: Wenn die Stylesheet-Datei leer ist.
        Exception: Wenn ein anderer Fehler beim Laden oder Anwenden des Stylesheets auftritt.
    """

    try:
        logger.info(f"Beginne, das Stylesheet '{stylesheet_name}' zu laden.")  # Startmeldung

        # Absoluter Pfad zur QSS-Datei bestimmen
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Verzeichnis bestimmen
        stylesheet_path = os.path.join(base_dir, stylesheet_name)

        # Prüfen, ob die Datei existiert
        if not os.path.exists(stylesheet_path):
            error_message = f"Stylesheet '{stylesheet_name}' wurde nicht gefunden unter {stylesheet_path}"
            logger.error(error_message)
            raise FileNotFoundError(error_message)

        # Prüfen, ob die Datei Inhalt hat
        if os.path.getsize(stylesheet_path) == 0:
            error_message = f"Stylesheet '{stylesheet_name}' ist leer."
            logger.error(error_message)
            raise ValueError(error_message)

        # Stylesheet laden und anwenden
        with open(stylesheet_path, "r") as file:
            app.setStyleSheet(file.read())
            logger.info(f"Stylesheet '{stylesheet_name}' erfolgreich angewendet.")

    except Exception as e:
        logger.error(f"Fehler beim Verarbeiten des Stylesheets '{stylesheet_name}': {e}", exc_info=True)
        raise
