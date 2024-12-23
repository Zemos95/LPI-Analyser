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
import sys 
from src.utils.logging_setup import logging
from gui import run_app
#from utils.logging_setup import initialize_logging  # Logging-Setup importieren
from utils.exception_setup import CustomException

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
        print("Initialisierung des Fehlerspeichers..")
        #initialize_logging()
        logging.info("Fehlerspeicher wurde erfolgreich gestartet.")
        

        # Schritt 2: Starten der GUI
        print("Starte GUI")
        run_app()
        logging.info("LPI-Analyser wurde erfolgreich gestartet.")
    except Exception as e:
        logging.info("Ein unerwarteter Fehler ist aufgetreten")
        raise CustomException(e, sys)
if __name__ == '__main__':
    main()