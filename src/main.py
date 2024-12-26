"""
main.py

Dies ist der Einstiegspunkt der Anwendung. 
Die GUI wird über die Klasse `ApplicationWindow` gestartet.

Funktionen:
- `main()`: Initialisiert die GUI und startet die Anwendung.

Abhängigkeiten:
- PyQt5
- application_window aus dem `gui`-Modul
"""

# Import
from src.gui import run_app
from src.utils.logging_setup import Logger  


def main() -> None:
    """
    Dies ist die main-Funktion über die die gesamte Software gestartet wird.
    ----
    Input: None
    ----
    Output: None
    """
    # Schritt 1: Initialisierung des Logging-Systems
    try: 
        # Initialisierung des Loggers
        logger_instance = Logger(name="LPI-Analyser", log_file="LPI_analyser_logfile.log", level="INFO")
        logger = logger_instance.get_logger()
        logger.info("Logger wurde erfolgreich gestartet.")
        

        # Starten der GUI
        run_app()
        logger.info("LPI-Analyser wurde erfolgreich gestartet.")

    except Exception as e:
        logger.error("Ein Fehler ist aufgetreten: {e}")
        raise
if __name__ == '__main__':
    main()