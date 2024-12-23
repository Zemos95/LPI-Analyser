"""
__init__.py

Dieses Skript enthält den Startpunkt der GUI. 

Funktionen:
- **runapp**: Initialiseiert die QApllication  und startet das Hauptfenster
---
Input: None
Output: None
"""


# Import
from PyQt6.QtWidgets import QApplication
from .application_window import ApplicationWindow
import sys

def run_app() -> None:
    """Initialisert QApplication und starten des Hauptfensters."""

    app = QApplication(sys.argv)
    window = ApplicationWindow()
    window.show()
    sys.exit(app.exec())