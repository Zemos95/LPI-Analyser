"""
menu.py

Dieses Skript enthält benutzerdefinierte Klassen zur Implementierung einer Menüleiste und einer Statusleiste 
für eine PyQt-Anwendung.

Klassen:
- **MenuBar**: Repräsentiert die benutzerdefinierte Menüleiste und enthält Signal- und Menülogik.
- **StatusBar**: Repräsentiert die benutzerdefinierte Statusleiste und bietet Methoden zur Anzeige von Nachrichten.
"""


# Imports
from PyQt6.QtWidgets import QMenuBar, QStatusBar, QLabel
from PyQt6.QtCore import pyqtSignal, QTimer
from PyQt6.QtGui import QAction
import psutil

class MenuBar(QMenuBar):
    """
    Eine benutzerdefinierte Klasse, die von QMenuBar erbt. Die Klasse definiert Menüs und Aktionen für 
    die Benutzeroberfläche und enthält ein Signal zur Rainflow-Aktion.

    Attribute:
        rainflow_triggered (pyqtSignal): Signal, das ausgelöst wird, wenn die Rainflow-Aktion gestartet wird.
    """

    rainflow_triggered: pyqtSignal = pyqtSignal()
    fft_triggered: pyqtSignal = pyqtSignal()

    def __init__(self) -> None:
        """
        Initialisiert die MenuBar und ruft die Methode `init_menu` auf, um Menüs und Aktionen zu erstellen.
        """
        super().__init__()
        self.init_menu()

    def init_menu(self) -> None:
        """
        Erstellt die Menüs und Aktionen für die Menüleiste, einschließlich Datei-, Analyse- und Hilfe-Menüs.
        """
        # Erstellung "Datei-Menü"
        data_menu = self.addMenu("Datei")

        # Aktion: Öffnen
        open_action = QAction("Öffnen", self)
        open_action.triggered.connect(self.open_file)
        data_menu.addAction(open_action)

        # Aktion: Speichern
        save_action = QAction("Speichern", self)
        save_action.triggered.connect(self.save_file)
        data_menu.addAction(save_action)

        # Erstellung "Analyse-Menü"
        analyse_menu = self.addMenu("Analyse")

        # Aktion: Rainflow Analyse
        rainflow_action = QAction("Rainflow", self)
        rainflow_action.triggered.connect(self.emit_rainflow)
        analyse_menu.addAction(rainflow_action)

        # Aktion: FFT-Analyse
        fft_action = QAction("FFT", self)
        fft_action.triggered.connect(self.emit_fft)
        analyse_menu.addAction(fft_action)

        # Erstellung "Hilfe-Menü"
        help_menu = self.addMenu("Hilfe")

        # Aktion: Über
        about_action = QAction("Über", self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)

    
    def open_file(self) -> None:
        """
        Slot für die Öffnen-Aktion. Führt die Logik zum Öffnen einer Datei aus.
        """
        pass

    
    def save_file(self) -> None:
        """
        Slot für die Speichern-Aktion. Führt die Logik zum Speichern einer Datei aus.
        """
        pass

    
    def emit_rainflow(self) -> None:
        """
        Löst das Signal `rainflow_triggered` aus, das mit der Rainflow-Analyse verknüpft ist.
        """
        self.rainflow_triggered.emit()

    
    def emit_fft(self) -> None:
        """
        Slot für die FFT-Analyse-Aktion. Führt die Logik zur FFT-Analyse aus.
        """
        self.fft_triggered.emit()

    
    def show_about_dialog(self) -> None:
        """
        Slot für die Über-Aktion. Zeigt einen Dialog mit Informationen über die Anwendung an.
        """
        pass


class StatusBar(QStatusBar):
    """
    Eine benutzerdefinierte Klasse, die von QStatusBar erbt. Die Klasse bietet Funktionen zur Anzeige von Statusmeldungen bzw. Statusinformationen
    """
    def __init__(self) -> None:
        """
        Initialisiert die StatusBar.
        """
        super().__init__()
        self.init_cpu_ram_status()


    def init_cpu_ram_status(self) -> None:
        # Erstelle Labels für CPU- und RAM-Auslastung
        self.cpu_label = QLabel("CPU: 0%")
        self.ram_label = QLabel("RAM: 0%")

        # Füge die Labels zur Statusleiste hinzu
        self.addPermanentWidget(self.cpu_label)
        self.addPermanentWidget(self.ram_label)

        # Timer für regelmäiges Update
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_system_stats)
        self.update_timer.start(1000) # Aktualisiere alle 1000 ms
    
    def update_system_stats(self) -> None:
        """
        Aktualsiere die CPU und RAM-Auslastung und zeigt sie in der Statusleiste an
        """
        cpu_usage = psutil.cpu_percent(interval=0)
        ram_usage = psutil.virtual_memory().percent

        self.cpu_label.setText(f"CPU: {cpu_usage}%")
        self.ram_label.setText(f"RAM: {ram_usage}%")


    def show_rainflow_start_status(self) -> None:
        """
        Zeigt eine Nachricht in der Statusleiste an, die den Benutzer darüber informiert, dass die Rainflow-Anwendung gestartet wird.
        """
        self.showMessage("Die Rainflow-Anwendung wird gestartet...", 2000)
    

    def show_fft_start_status(self) -> None:
        """
        Zeiogt eine Nachricht in der Statusleiste an, die den Benutzer darüber informiert, dass die Rainflow-Anwendung gestartet wird.
        """
        self.showMessage("Die FFT-Anwendung wird gestartet...", 2000)


