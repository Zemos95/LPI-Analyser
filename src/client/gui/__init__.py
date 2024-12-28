import sys
import logging
from PyQt6.QtWidgets import QApplication, QDialog
from src.client.gui.main_window import MainWindow
from src.client.gui.styles import apply_stylesheet
from src.client.gui.dialogs.login_dialog import LoginDialog


def run_app(logger: logging.Logger) -> None:
    """
    Initialisiert QApplication und startet das Hauptfenster.
    """
    try:
        logger.info("Initialisiere QApplication.")
        app = QApplication(sys.argv)
    except Exception as e:
        error_type = type(e).__name__  # Typ der Ausnahme
        logger.error(f"Die QApplication konnte nicht initialisiert werden: ({error_type}) {e}")
        raise
    
    # Login-Dialog
    try:
        logger.info("Zeige Login-Fenster an.")
        login_dialog = LoginDialog(logger)
        if login_dialog.exec() != QDialog.DialogCode.Accepted:
            logger.warning("Login abgebrochen. Anwendung wird beendet.")
            app.quit()
            return
        logger.info("Login erfolgreich. Benutzer hat sich angemeldet.")
    except Exception as e:
        error_type = type(e).__name__  # Typ der Ausnahme
        logger.error(f"Fehler beim Login-Fenster: ({error_type}) {e}")
        raise

    # Stylesheet anwenden
    try:
        logger.info("Wende Stylesheet an.")
        apply_stylesheet(app, "app_styles.qss", logger)
    except Exception as e:
        error_type = type(e).__name__  # Typ der Ausnahme
        logger.error(f"Das Stylesheet konnte nicht ausgeführt werden: ({error_type}) {e}")
        raise

    # Hauptfenster starten
    try:
        logger.info("Starte Hauptfenster.")
        window = MainWindow()
        window.show()
    except Exception as e:
        error_type = type(e).__name__  # Typ der Ausnahme
        logger.error(f"Das Hauptfenster konnte nicht gestartet werden: ({error_type}) {e}")
        raise

    # Anwendung ausführen
    try:
        logger.info("Anwendung wird gestartet.")
        sys.exit(app.exec())
    except Exception as e:
        error_type = type(e).__name__  # Typ der Ausnahme
        logger.error(f"Ein Fehler ist aufgetreten: ({error_type}) {e}")
        raise
