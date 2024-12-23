import os
import sys
from src.utils.logging_setup import logging
from PyQt6.QtWidgets import QApplication
from utils.exception_setup import CustomException

def apply_stylesheet(app: QApplication, stylesheet_name: str) -> None:
    """
    Lädt und wendet ein Stylesheet (QSS-Datei) auf die Anwendung an.

    Args:
        app (QApplication): Die PyQt-Anwendung.
        stylesheet_name (str): Der Name der Stylesheet-Datei im Verzeichnis `styles`.

    Raises:
        CustomException: Wenn die Stylesheet-Datei nicht gefunden wird, leer ist oder ein Fehler beim Laden auftritt.
    """
    try:
        logging.info(f"Beginne, das Stylesheet '{stylesheet_name}' zu laden.")  # Startmeldung
    except Exception as e:
        logging.info("Fehler beim Starten der Stylesheet-Operation.")
        raise CustomException(e, sys)

    # Absoluter Pfad zur QSS-Datei bestimmen
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Verzeichnis `styles`
        stylesheet_path = os.path.join(base_dir, stylesheet_name)
    except Exception as e:
        logging.info("Fehler beim Erstellen des Pfads zur Stylesheet-Datei.")
        raise CustomException(e, sys)

    # Prüfen, ob die Datei existiert
    try:
        if not os.path.exists(stylesheet_path):
            logging.info(f"Stylesheet '{stylesheet_name}' wurde nicht gefunden unter {stylesheet_path}")
            raise FileNotFoundError(f"Stylesheet '{stylesheet_name}' wurde nicht gefunden.")
    except Exception as e:
        logging.info("Fehler beim Überprüfen der Existenz der Stylesheet-Datei.")
        raise CustomException(e, sys)

    # Prüfen, ob die Datei Inhalt hat
    try:
        if os.path.getsize(stylesheet_path) == 0:
            logging.info(f"Stylesheet '{stylesheet_name}' ist leer.")
            raise ValueError(f"Stylesheet '{stylesheet_name}' ist leer.")
    except Exception as e:
        logging.info("Fehler beim Überprüfen der Dateigröße.")
        raise CustomException(e, sys)

    # Stylesheet laden und anwenden
    try:
        with open(stylesheet_path, "r") as file:
            app.setStyleSheet(file.read())
            logging.info(f"Stylesheet '{stylesheet_name}' erfolgreich angewendet.")
    except Exception as e:
        logging.info("Fehler beim Laden und Anwenden des Stylesheets.")
        raise CustomException(e, sys)
