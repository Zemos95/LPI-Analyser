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
import os
from src.utils.logging_setup import logging
from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6.QtGui import QPainter, QPixmap, QIcon
from PyQt6.QtCore import Qt
from gui.widgets.menus import MenuBar, StatusBar




class MainWindow(QMainWindow):
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
        # Setze Geometry der Applikation auf volle Bildschirmgröße
        self.showMaximized()
        # Pfad zum Hintergrundbild"
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.background_image_path = os.path.join(self.current_dir, "resources/images/lpi_background_image.png")
        # Pfad zum logo
        self.icon_path = os.path.join(self.current_dir, "resources/images/logo.png")
        # Füge Initialisierung der UI hinzu
        self.init_ui()

      
    def paintEvent(self, event) -> None:
        """Stellt ein Hintergrundbild da:
        ---
        Input: self
        ---
        Output: None
        """
        painter = QPainter(self)
        pixmap = QPixmap(self.icon_path)
        if not pixmap.isNull(): # Uberprüfung, ob das Bild geladen werden konnte
            # Hole die Originalgröße des Bildes (falls nötig, überprüfe die Skalierungsoptionen)
            pixmap = pixmap.scaledToWidth(pixmap.width(), Qt.TransformationMode.SmoothTransformation)
            # Originalgröße des Pixmaps
            pixmap_width = pixmap.width()
            pixmap_height = pixmap.height()

            # Fenstergröße
            window_width = self.width()
            window_height = self.height()

            # Berechne die Position, um das Bild zu zentrieren
            x = (window_width - pixmap_width) // 2
            y = (window_height - pixmap_height) // 2

            # Zeichne das Bild in Originalgröße zentriert
            painter.drawPixmap(x, y, pixmap)
        else:
          logging.info("Hintergrundbild konnte nicht geladen werden: {self.background_image_path}")
        #painter.drawPixmap(self.rect(), pixmap)
    
    def get_window_icon(self) -> QIcon:
        """
        Lädt das Fenster-Icon.

        Returns:
            QIcon: Das Fenster-Icon.
        """
        
        if os.path.exists(self.icon_path):
            return QIcon(self.icon_path)
        else:
            logging.warning(f"Fenster-Icon nicht gefunden: {self.icon_path}")
            return QIcon()

    def init_ui(self) -> None:
        """Bindet die Benutzeroberfläche an das Hauptfenster."""
        
        # Statusleisteeinfügen
        self.status_bar = StatusBar()
        self.setStatusBar(self.status_bar)

        # Menüleiste einfügen
        self.menu_bar = MenuBar() # Erstellung Menüleiste
        self.menu_bar.rainflow_env_start_triggered.connect(self.status_bar.show_status) # Verbindung Menu/Status-Bar
        self.menu_bar.fft_env_start_triggered.connect(self.status_bar.show_status) # Verbindung Menu/Status-Bar
        self.menu_bar.monitoring_viewer_start_triggered.connect(self.status_bar.show_status)
        # Setzen der Menüleiste
        self.setMenuBar(self.menu_bar)
