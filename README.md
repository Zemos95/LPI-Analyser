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

- **`requirements.txt`**: Liste der Python-Abhängigkeiten für das Projekt.

- **`setup.py`**: Setup-Datei zur Installation des Projekts.

- **`README.md`**: Dokumentation des Projekts.

- **`LICENSE`**: Lizenzdatei für das Projekt.

