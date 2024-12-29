from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from src.client.services.auth_manager import authenticate_user
import logging
import requests


class LoginDialog(QDialog):
    """
    Ein einfaches Login-Fenster, das den Benutzer nach einem Benutzernamen und Passwort fragt.
    """

    def __init__(self, logger: logging.Logger, parent=None):
        """Initialisierung der Klasse LoginDialog"""
        super().__init__(parent)
        self.logger = logger
        self.setWindowTitle("Anmeldung")
        self.setFixedSize(400, 200)

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
            # Serverkommunikation ausführen
            response = authenticate_user(username, password, self.logger)

            # Antwort vom Server verarbeiten
            server_response = response.json()
            if server_response.get("success"):
                QMessageBox.information(self, "Erfolg", server_response.get("message"))
                self.accept()  # Schließt den Dialog und gibt Erfolg zurück
            else:
                QMessageBox.warning(self, "Fehler", server_response.get("message"))

        except requests.HTTPError as http_err:
            QMessageBox.warning(self, "Fehler", f"HTTP-Fehler: {http_err}")

        except requests.RequestException:
            QMessageBox.critical(self, "Fehler", "Kommunikation mit dem Server fehlgeschlagen.")

        except Exception as e:
            QMessageBox.critical(self, "Fehler", "Ein unerwarteter Fehler ist aufgetreten.")
