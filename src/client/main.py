
# Import
from src.client.gui import run_app
from src.client.utils.client_logging_setup import Logger  


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
        logger_instance = Logger(name="LPI-Analyser", log_file="LPI_Analyser_UI_logfile.log", level="INFO")
        logger = logger_instance.get_logger()
        logger.info("Logger wurde erfolgreich gestartet.")
    except Exception as e:
        raise ValueError("Logger wurde nicht gestartet.") from e
    
    try:
        # Starten der GUI
        logger.info("Starte GUI-Anwendung")
        run_app(logger)

    except Exception as e:
        error_type = type(e).__name__  # Typ der Ausnahme
        logger.error(f"Ein Fehler ist aufgetreten: ({error_type}) {e}")
        raise
    logger.info("LPI-Analyser wurde erfolgreich gestartet.")
if __name__ == '__main__':
    main()