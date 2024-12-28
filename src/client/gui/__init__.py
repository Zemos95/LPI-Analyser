import sys
from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow
from gui.styles import apply_stylesheet
from src.utils.logging_setup import Logger  # Importiere den Logger

def run_app() -> None:
    """
    Initialisiert QApplication und startet das Hauptfenster.
    """
    logger = Logger().get_logger()  # Logger abrufen
    try:
        logger.info("Initialisiere QApplication.")
        app = QApplication(sys.argv)

        logger.info("Wende Stylesheet an.")
        apply_stylesheet(app, "app_styles.qss")

        logger.info("Starte Hauptfenster.")
        window = MainWindow()
        window.show()

        logger.info("Anwendung wird gestartet.")
        sys.exit(app.exec())
    except Exception as e:
        logger.error("Ein Fehler ist während der Ausführung von run_app aufgetreten: %s", e, exc_info=True)
        raise
