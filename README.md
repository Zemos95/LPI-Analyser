
# LPI-Analyser

Ein Python-basiertes Tool zur Rainflow- und FFT-Analyse, mit einer benutzerfreundlichen Oberfläche und modularer Architektur.

---

## Projektstruktur

- **`src/`**: Hauptquellcode des Projekts.
  - **`main.py`**: Einstiegspunkt der Anwendung. Startet die GUI und initialisiert alle Module.
  - **`pipelines/`**: Enthält Module zur Verarbeitung von Datenquellen.
    - **`ubdf_reader.py`**: Modul zum Lesen und Parsen von UBDF-Dateien.
    - **`file_reader.py`**: Allgemeiner Datei-Lesezugriff, z. B. für Text- oder CSV-Dateien.
    - **`db_connector.py`**: Verbindung und Abfragen von Datenbanken.
    - **`server_connector.py`**: Modul zum Abrufen von Daten von externen Servern oder APIs.
  - **`processing/`**: Implementiert Analysen und Datenaufbereitung.
    - **`rainflow_analysis.py`**: Implementierung der Rainflow-Analyse zur Ermüdungsbewertung.
    - **`fft_analysis.py`**: Implementierung der Fast-Fourier-Transformation (FFT) zur Signalverarbeitung.
  - **`gui/`**: Benutzeroberfläche mit PyQt.
    - **`application_window.py`**: Hauptfenster der GUI. Organisiert das Layout und die zentrale Steuerung.
    - **`dialogs/`**: Beinhaltet verschiedene Dialogfenster.
      - **`settings_dialog.py`**: Dialog für Benutzereinstellungen.
      - **`about_dialog.py`**: Dialog zur Anzeige von Informationen über die Anwendung.
    - **`widgets/`**: Benutzerdefinierte Widgets für komplexere GUI-Komponenten.
      - **`chart_widgets.py`**: Widgets zur Darstellung von Diagrammen.
      - **`result_widgets.py`**: Widgets zur Anzeige von Analyseergebnissen.
    - **`styles/`**: QSS-Dateien zur Gestaltung der GUI.
      - **`app_styles.qss`**: Stylesheet für die Hauptfenster der Anwendung.
      - **`widget_styles.qss`**: Stylesheet für individuelle Widgets.
    - **`resources/`**: Enthält alle Ressourcen wie Icons und Bilder.
      - **`icons/`**: Icons für die GUI, z. B.:
        - **`app_icon.png`**: Haupticon der Anwendung.
        - **`settings_icon.png`**: Icon für den Einstellungsdialog.
      - **`images/`**: Enthält Bilder wie das Projektlogo.
        - **`logo.png`**: Logo der Anwendung.
      - **`resources.qrc`**: Qt-Ressourcendatei zur Organisation der Ressourcen.
    - **`helpers/`**: Hilfsfunktionen für die GUI.
      - **`layout_helpers.py`**: Funktionen zur dynamischen Anpassung von Layouts.
      - **`signal_helpers.py`**: Hilfsfunktionen für Signal- und Slot-Management in PyQt.
  - **`utils/`**: Nützliche Funktionen und Tools.
    - **`file_operations.py`**: Funktionen für Dateioperationen wie Lesen und Schreiben.
    - **`logging_setup.py`**: Setup und Konfiguration für das Logging.
    - **`math_tools.py`**: Enthält mathematische Hilfsfunktionen.
    - **`exception_setup.py`**: Definiert benutzerdefinierte Ausnahmen und Fehlerklassen.

- **`tests/`**: Enthält alle Unit-Tests für das Projekt.
  - **`pipelines/`**: Tests für die Module im Ordner `pipelines`.
    - **`test_ubdf_reader.py`**: Tests für das Modul `ubdf_reader`.
    - **`test_file_reader.py`**: Tests für das Modul `file_reader`.
    - **`test_db_connector.py`**: Tests für das Modul `db_connector`.
    - **`test_server_connector.py`**: Tests für das Modul `server_connector`.
  - **`processing/`**: Tests für die Analyse- und Verarbeitungslogik.
    - **`test_rainflow_analysis.py`**: Tests für die Rainflow-Analyse.
    - **`test_fft_analysis.py`**: Tests für die FFT-Analyse.
  - **`gui/`**: Tests für die Benutzeroberfläche.
    - **`test_application_window.py`**: Tests für das Hauptfenster der GUI.
    - **`dialogs/`**: Tests für die Dialoge.
      - **`test_settings_dialog.py`**: Tests für den Einstellungsdialog.
      - **`test_about_dialog.py`**: Tests für den Über-Dialog.
    - **`widgets/`**: Tests für benutzerdefinierte Widgets.
      - **`test_chart_widgets.py`**: Tests für das Modul `chart_widgets`.
      - **`test_result_widgets.py`**: Tests für das Modul `result_widgets`.
    - **`helpers/`**: Tests für die GUI-Hilfsfunktionen.
      - **`test_layout_helpers.py`**: Tests für das Modul `layout_helpers`.
      - **`test_signal_helpers.py`**: Tests für das Modul `signal_helpers`.
  - **`utils/`**: Tests für die Hilfsfunktionen.
    - **`test_file_operations.py`**: Tests für Dateioperationen.
    - **`test_logging_setup.py`**: Tests für das Logging-Setup.
    - **`test_math_tools.py`**: Tests für mathematische Funktionen.
    - **`test_exception_setup.py`**: Tests für benutzerdefinierte Fehler.

- **`logs/`**: Enthält Log-Dateien zur Fehlerdiagnose.
  - **`app.log`**: Hauptlogdatei der Anwendung.
- **`.dockerignore`**: Enthält alle Informationen die beim "build" des Dockers ignoriert werden.
- **`.gitignore`**: Enthält alle Informationen die beim Hochladen in git ignoriert werden.
- **`..github`**:Enthält den Ordner workflows
  - - **`.ci.yml`**: Enthält die CI-Pipline Information-
- **`LICENSE`**: Lizenzdatei für das Projekt.
- **`pyproject.toml`**: Setup-Datei zur Installation des Projekts.

- **`README.md`**: Dokumentation des Projekts.

---

## Installation

### Voraussetzungen
1. Installiere Python 3.10 oder höher.
2. Stelle sicher, dass `pip` und `virtualenv` installiert sind:
   ```bash
   pip install --upgrade pip
   pip install virtualenv
   ```

### Schritte
1. **Repository klonen**:
   ```bash
   git clone <repository-url>
   cd LPI-Analyser
   ```

2. **Virtuelles Environment erstellen und aktivieren**:
   - **Windows**:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Abhängigkeiten installieren**:
   Führe im Projektverzeichnis den folgenden Befehl aus:
   ```bash
   pip install .
   ```

4. **Projekt starten**:
   ```bash
   python src/main.py
   ```
---

## GUI

### Signal-Slot-Mechanismus

Das Projekt verwendet das Signal-Slot-System von PyQt, um lose gekoppelte Interaktionen zwischen GUI-Komponenten zu ermöglichen.

#### Ablauf:
1. Der Benutzer klickt in der `MenuBar` auf "Rainflow".
2. Das `triggered`-Signal der `QAction` löst die Methode `emit_rainflow` in der `MenuBar` aus.
3. Die Methode `emit_rainflow` ruft `self.rainflow_triggered.emit()` auf.
4. Das benutzerdefinierte Signal `rainflow_triggered` wird ausgelöst.
5. Im `ApplicationWindow` wird das Signal `rainflow_triggered` mit dem Slot `show_rainflow_status` in der `StatusBar` verbunden.
6. Der Slot `show_rainflow_status` zeigt die Nachricht "Die Rainflow-Anwendung wird gestartet..." in der Statusleiste an.

### Klassenübersicht:
- **MenuBar**:
  - Enthält das Signal `rainflow_triggered`.
  - Sendet das Signal, wenn der Benutzer auf "Rainflow" klickt.

- **StatusBar**:
  - Enthält den Slot `show_rainflow_status`.
  - Reagiert auf das Signal `rainflow_triggered`.

- **ApplicationWindow**:
  - Verbindet das Signal `rainflow_triggered` aus der `MenuBar` mit dem Slot `show_rainflow_status` in der `StatusBar`.
