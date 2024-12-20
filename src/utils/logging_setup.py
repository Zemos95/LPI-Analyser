"""
logging_setup.py

Dieses Skript richtet ein Logging-System ein, um konsistente und strukturierte Log-Dateien in Python-Anwendungen zu erstellen.

Funktionen:
- Erzeugt eine Log-Datei mit einem Zeitstempel im Dateinamen.
- Erstellt automatisch ein Verzeichnis "logs", falls es nicht existiert.
- Konfiguriert die Logging-Einstellungen, einschließlich Dateispeicherort, Format und Log-Level.

Details der Konfiguration:
- **log_file**: Speichert den Namen der Log-Datei, der mit dem aktuellen Datum und der Uhrzeit generiert wird.
- **log_path**: Speichert den Pfad des Verzeichnisses, in dem die Log-Datei abgelegt wird.
- **basicConfig**:
  - **filename**: Legt fest, in welcher Datei die Logs gespeichert werden.
  - **format**: Definiert das Format der Log-Einträge:
    - **%(asctime)s**: Zeitstempel des Log-Eintrags.
    - **%(lineno)d**: Zeilennummer, in der das Log erstellt wurde.
    - **%(name)s**: Name des Loggers.
    - **%(levelname)s**: Schweregrad des Logs (z. B. INFO, ERROR).
    - **%(message)s**: Inhalt der Log-Nachricht.
  - **level**: Definiert die minimale Log-Ebene (standardmäßig `logging.INFO`).
"""

# Import der benötigten Module
import logging
import os
from datetime import datetime

# Schritt 1: Generierung des Log-Dateinamens (mit Zeitstempel)
log_file = f"{datetime.now(tz=None).strftime('%m_%d_%Y_%H_%M_%S')}_logfile.log"  # Beispiel: 12_20_2024_15_30_45_logfile.log

# Schritt 2: Festlegung des Log-Verzeichnisses
log_path = os.path.join(os.getcwd(), "logs")  # Das "logs"-Verzeichnis wird im aktuellen Arbeitsverzeichnis erstellt

# Schritt 3: Erstellung des Log-Verzeichnisses (falls nicht vorhanden)
os.makedirs(log_path, exist_ok=True)

# Schritt 4: Kombination von Verzeichnis und Dateiname zu einem vollständigen Pfad
log_file_path = os.path.join(log_path, log_file)

# Schritt 5: Konfiguration des Logging-Systems
logging.basicConfig(
    filename=log_file_path,  # Speicherort der Log-Datei
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Log-Format
    level=logging.INFO,  # Log-Level: Erfasst alle Nachrichten ab INFO
)

# Hinweis:
# - Dieses Skript wird beim Import automatisch ausgeführt und erstellt die Log-Datei im definierten Verzeichnis.
# - Die Konfiguration kann bei Bedarf angepasst werden, um unterschiedliche Formate oder Log-Levels zu verwenden.
