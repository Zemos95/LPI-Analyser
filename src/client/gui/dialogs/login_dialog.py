import requests
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import logging

class LoginDialog(QDialog):
    """
    Ein einfaches Login-Fenster, das den Benutzer nach einem Benutzernamen und Passwort fragt.
    """

    def __init__(self, logger: logging.Logger, parent=None):
        """Initialisierung der Klasse LoginDialog"""
        super().__init__(parent)
        self.logger = logger
        self.setWindowTitle("Anmeldung")
        self.setFixedSize(300, 150)

        # UI-Komponenten
        self.username_label = QLabel("Benutzername:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Passwort:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Anmelden")
        self.cancel_button = QPushButton("Abbrechen")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.cancel_button)
        self.setLayout(layout)

        # Verbindungen
        self.login_button.clicked.connect(self.validate_credentials)
        self.cancel_button.clicked.connect(self.reject)

    def validate_credentials(self):
        """
        Überprüft die Anmeldedaten durch Kommunikation mit dem Server.
        """
        username = self.username_input.text()
        password = self.password_input.text()

        try:
            # Anfrage an den Flask-Server
            response = requests.post(
                "http://127.0.0.1:5000/login",
                json={"username": username, "password": password}
            )

            if response.status_code == 200 and response.json().get("success"):
                QMessageBox.information(self, "Erfolg", response.json().get("message"))
                self.logger.info(f"Benutzer {username} hat sich erfolgreich eingeloggt.")
                self.accept()  # Schließt den Dialog und gibt Erfolg zurück
            else:
                QMessageBox.warning(self, "Fehler", response.json().get("message"))
                self.logger.warning(f"Benutzer {username} konnte sich nicht erfolgreich einloggen.")
        except requests.RequestException as e:
            self.logger.error(f"Fehler bei der Kommunikation mit dem Server: {e}")
            QMessageBox.critical(self, "Fehler", "Kommunikation mit dem Server fehlgeschlagen.")
