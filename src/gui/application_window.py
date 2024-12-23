"""
application_window.py

Signal-Slot-Mechanismus:

1. Der Benutzer klickt in der `MenuBar` auf "Rainflow".
2. Das `triggered`-Signal der `QAction` löst die Methode `emit_rainflow` in der `MenuBar` aus.
3. Die Methode `emit_rainflow` ruft `self.rainflow_triggered.emit()` auf.
4. Das benutzerdefinierte Signal `rainflow_triggered` wird ausgelöst.
5. Im `ApplicationWindow` wird das Signal `rainflow_triggered` mit dem Slot `show_rainflow_status` in der `StatusBar` verbunden.
6. Der Slot `show_rainflow_status` zeigt die Nachricht "Die Rainflow-Anwendung wird gestartet..." in der Statusleiste an.

Zusammenhängende Klassen:
- MenuBar:
  - Enthält das Signal `rainflow_triggered`.
  - Sendet das Signal, wenn der Benutzer auf "Rainflow" klickt.
- StatusBar:
  - Enthält den Slot `show_rainflow_status`.
  - Reagiert auf das Signal `rainflow_triggered`.
- ApplicationWindow:
  - Verbindet das Signal `rainflow_triggered` aus der `MenuBar` mit dem Slot `show_rainflow_status` in der `StatusBar`.

---

Dieses Skript enthält die Klasse `ApplicationWindow`, die das Hauptfenster der Anwendung definiert.
Die Klasse erbt von QMainWindow und integriert die Statusleiste und Menüleiste in die GUI.

Klassen:
- **ApplicationWindow**: Repräsentiert das Hauptfenster der Anwendung.

Methoden:
- **__init__**: Initialisiert das Hauptfenster mit Titel, Größe und UI-Komponenten.
- **init_ui**: Bindet die Status- und Menüleiste in das Hauptfenster ein und verknüpft Signale mit Slots.
"""

# Import
from PyQt6.QtWidgets import QMainWindow
from gui.widgets.menus import MenuBar, StatusBar


class ApplicationWindow(QMainWindow):
    """
    Repräsentiert das Hauptfenster der Anwendung. Diese Klasse erbt von QMainWindow und fügt benutzerdefinierte 
    GUI-Komponenten wie eine Menüleiste und eine Statusleiste hinzu.
    
    Attribute:
        status_bar (StatusBar): Die Statusleiste des Hauptfensters.
        menu_bar (MenuBar): Die Menüleiste des Hauptfensters.
    """

    def __init__(self) -> None:
        """
        Initialisiert das Hauptfenster der Anwendung.
        
        Funktionen:
        - Setzt den Fenstertitel und die Größe.
        - Ruft `init_ui` auf, um die Benutzeroberfläche zu erstellen.
        """
        super().__init__()
        self.setWindowTitle("LPI-Analyser")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self) -> None:
        """
        Bindet die Benutzeroberfläche an das Hauptfenster.
        
        Funktionen:
        - Fügt die Statusleiste ein und setzt sie in das Hauptfenster.
        - Fügt die Menüleiste ein und verbindet Signale mit Slots.
        """
        # Statusleiste einfügen
        self.status_bar = StatusBar()
        # Statusleiste einfügen
        self.setStatusBar(self.status_bar)

        # Menüleiste einfügen
        self.menu_bar = MenuBar() # Erstellung Menüleiste
        self.menu_bar.rainflow_triggered.connect(self.status_bar.show_rainflow_start_status) # Verbindung Menu/Status-Bar
        self.menu_bar.fft_triggered.connect(self.status_bar.show_fft_start_status) # Verbindung Menu/Status-Bar
        # Setzen der Menüleiste
        self.setMenuBar(self.menu_bar)
