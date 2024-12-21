import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor

class GUI:
    def __init__(self):
        print("Initialisiere GUI...")
        self.app = QApplication(sys.argv)

        # Hauptfenster erstellen
        self.window = QWidget()
        self.window.setWindowTitle("Test GUI")
        self.window.setGeometry(100, 100, 400, 300)  # Breite x Höhe
        self.init_ui()

        self.window.show()
        print("GUI gestartet...")
        sys.exit(self.app.exec())

    def init_ui(self):
        # Layout für das Hauptfenster erstellen
        layout = QVBoxLayout()

        # Schwarzer Kasten erstellen
        black_box = QWidget()
        black_box.setFixedSize(100, 100)  # Größe des Kastens
        black_box.setAutoFillBackground(True)

        # Hintergrundfarbe auf Schwarz setzen
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(Qt.GlobalColor.black))
        black_box.setPalette(palette)

        # Debug-Ausgabe
        print("Schwarzer Kasten erstellt!")

        # Kasten zum Layout hinzufügen
        layout.addWidget(black_box)

        # Layout dem Hauptfenster zuweisen
        self.window.setLayout(layout)
