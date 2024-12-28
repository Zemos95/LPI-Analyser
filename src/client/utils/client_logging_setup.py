import logging
from logging.handlers import RotatingFileHandler
import os

class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Erstellt eine Singleton-Instanz der Logger-Klasse.
        """
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name: str, log_file: str, level: int = logging.INFO):
    #def __init__(self, name: str="LPI-Analyser", log_file: str = "LPI-Analyser_UI_logfile.log", level: int = logging.INFO):
        """
        Initialisiert den Logger.

        :param name: Name des Loggers
        :param log_file: Name der Log-Datei
        :param level: Logging-Level (z.B. logging.DEBUG, logging.INFO)
        """
        if not hasattr(self, "logger"):
            self.logger = logging.getLogger(name)
            self.logger.setLevel(level)

            # Sicherstellen, dass der Ordner "logs" existiert
            log_directory = os.path.join(os.getcwd(), "logs")
            os.makedirs(log_directory, exist_ok=True)

            # Log-Dateipfad erstellen
            log_file_path = os.path.join(log_directory, log_file)

            # Format für Logs
            log_format = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(pathname)s:%(lineno)d - %(message)s"
            )

            # Datei-Handler mit Rotating Logs
            file_handler = RotatingFileHandler(
                log_file_path, maxBytes=5 * 1024 * 1024, backupCount=3
            )
            file_handler.setFormatter(log_format)
            file_handler.setLevel(level)

            # Konsolen-Handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(log_format)
            console_handler.setLevel(level)

            # Handlers zum Logger hinzufügen
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def get_logger(self) -> logging.Logger:
        """Gibt den konfigurierten Logger zurück."""
        return self.logger
