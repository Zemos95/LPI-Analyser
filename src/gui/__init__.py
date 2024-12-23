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
import sys
import os
from PyQt6.QtWidgets import QApplication
from .application_window import ApplicationWindow
from .styles import apply_stylesheet



def run_app() -> None:
    """ Initialisert QApplication und starten des Hauptfensters. """

    app = QApplication(sys.argv)
    apply_stylesheet(app, "app_styles.qss")
    window = ApplicationWindow()
    window.show()
    sys.exit(app.exec())