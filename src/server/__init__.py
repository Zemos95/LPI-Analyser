from fastapi import FastAPI
from src.server.database.base import Base
from src.server.database.session import engine
from src.server.routes.auth_routes import router as auth_router
import logging

class Server:
    """
    Eine Klasse zur Initialisierung und Verwaltung des FastAPI-Servers.
    """
    def __init__(self, title: str = "LPI Analyser Server", version: str = "1.0"):
        """
        Initialisiert den Server.

        Args:
            title (str): Titel des Servers.
            version (str): Version des Servers.
        """
       # self.logger = logging.getLogger("Server")
        self.app = FastAPI(title=title, version=version)

        # Routen registrieren
        self._register_routes()

    def _register_routes(self):
        """Registriert API-Routen."""
        self.app.include_router(auth_router)
      #  self.logger.info("Routen erfolgreich registriert.")
        print("Routen erfolgreich registriert.")

    def initialize_database(self):
        """Initialisiert die Datenbank."""
        #self.logger.info("Initialisiere die Datenbank...")
        print("Initialisiere Datenbank...")
        Base.metadata.create_all(bind=engine)
       # self.logger.info("Datenbank erfolgreich initialisiert.")
        print("Datenbank erfolgreich initialisiert")

    def get_app(self):
        """
        Gibt die FastAPI-App zurück.

        Returns:
            FastAPI: Die FastAPI-Anwendung.
        """
        return self.app
