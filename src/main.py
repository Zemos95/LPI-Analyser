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
from gui import run_app

def main() -> None:
    """
    Dies ist die main-Funktion über die die gesamte Software gestartet wird.
    ----
    Input: None
    ----
    Output: None
    """

    print("Starte GUI")
    run_app()
if __name__ == '__main__':
    main()