import os
import logging
import pytest
from src.utils.logging_setup import Logger

@pytest.fixture
def logger_setup():
    """
    Fixture, um den Logger einzurichten und nach dem Test aufzuräumen.
    """
    # Logger initialisieren
    logger_instance = Logger(name="TestLogger", log_file="test_logger.log", level=logging.DEBUG)
    logger = logger_instance.get_logger()

    # Rückgabe des Loggers und des Log-Dateipfads
    log_file_path = os.path.join(os.getcwd(), "logs", "test_logger.log")
    yield logger, log_file_path

    # Nach dem Test die Log-Datei entfernen
    if os.path.exists(log_file_path):
        os.remove(log_file_path)


def test_logger_creation(logger_setup):
    """
    Testet, ob der Logger korrekt erstellt wird und Logs in die Datei schreibt.
    """
    logger, log_file_path = logger_setup

    # Schreibe eine Testnachricht
    logger.info("Test: Logger wurde erfolgreich erstellt.")
    
    # Prüfe, ob die Log-Datei erstellt wurde
    assert os.path.exists(log_file_path), "Die Log-Datei wurde nicht erstellt."

    # Prüfe den Inhalt der Log-Datei
    with open(log_file_path, "r") as log_file:
        logs = log_file.read()
        assert "Test: Logger wurde erfolgreich erstellt." in logs, "Die Log-Datei enthält nicht die erwartete Nachricht."


def test_logger_levels(logger_setup):
    """
    Testet, ob verschiedene Log-Levels korrekt verarbeitet werden.
    """
    logger, log_file_path = logger_setup

    # Schreibe Nachrichten auf verschiedenen Log-Levels
    logger.debug("Test: Debug-Nachricht.")
    logger.info("Test: Info-Nachricht.")
    logger.warning("Test: Warning-Nachricht.")
    logger.error("Test: Error-Nachricht.")
    logger.critical("Test: Critical-Nachricht.")

    # Prüfe den Inhalt der Log-Datei
    with open(log_file_path, "r") as log_file:
        logs = log_file.read()
        assert "Test: Debug-Nachricht." in logs, "Die Debug-Nachricht fehlt in der Log-Datei."
        assert "Test: Info-Nachricht." in logs, "Die Info-Nachricht fehlt in der Log-Datei."
        assert "Test: Warning-Nachricht." in logs, "Die Warning-Nachricht fehlt in der Log-Datei."
        assert "Test: Error-Nachricht." in logs, "Die Error-Nachricht fehlt in der Log-Datei."
        assert "Test: Critical-Nachricht." in logs, "Die Critical-Nachricht fehlt in der Log-Datei."


def test_logger_pathname(logger_setup):
    """
    Testet, ob der vollständige Pfad im Log korrekt gespeichert wird.
    """
    logger, log_file_path = logger_setup

    # Schreibe eine Nachricht
    logger.info("Test: Überprüfung des Pfads.")

    # Prüfe den Inhalt der Log-Datei
    with open(log_file_path, "r") as log_file:
        logs = log_file.read()
        assert __file__ in logs, "Der vollständige Pfad zum Testskript fehlt in der Log-Datei."
