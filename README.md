# LPI-Analyser

Ein Python-basiertes Tool zur Rainflow- und FFT-Analyse, mit einer benutzerfreundlichen Oberfläche und modularer Architektur.

---

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Features](#features)
- [Architektur](#architektur)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
  - [Client](#client)
  - [Server](#server)
- [Verwendung](#verwendung)
- [Projektstruktur](#projektstruktur)
- [Tests](#tests)
- [Lizenz](#lizenz)

---

## Überblick

Der LPI-Analyser besteht aus:
- **Client (Benutzeroberfläche):** Erstellt mit PyQt6 für eine einfache Bedienung und Benutzerinteraktion.
- **Server (Verarbeitung):** Implementiert mit FastAPI, führt Analysen wie FFT und Rainflow durch und verwaltet Authentifizierungen.

---

## Features

- **Modulare Architektur:**
  - Saubere Trennung von Client- und Serverlogik.
  - Leicht erweiterbar für zusätzliche Analysen oder Funktionen.
- **Benutzerfreundliche Oberfläche:**
  - PyQt6-basierte GUI für einfache Bedienung.
  - Echtzeit-Feedback und Ergebnisanzeige.
- **Serverbasierte Analysen:**
  - Fast Fourier Transformation (FFT).
  - Rainflow-Zählung für Ermüdungsanalysen.
- **Flexible Kommunikation:**
  - Client und Server kommunizieren über eine REST-API.
- **Protokollierung:**
  - Zentrale Log-Verwaltung für Client- und Serverereignisse.

---

## Architektur

Die Client-Server-Architektur ermöglicht eine klare Trennung von Benutzeroberfläche und Berechnungslogik:

1. **Client:**
   - Führt keine lokalen Berechnungen durch.
   - Sammelt Eingaben und zeigt Ergebnisse an.
   - Kommuniziert über HTTP mit dem Server.

2. **Server:**
   - Führt alle Berechnungen und Datenverarbeitungen durch.
   - Authentifiziert Benutzer.
   - Verwaltet Daten und Berechnungsergebnisse.

---

## Voraussetzungen

- **Python-Version:** `==3.11.11`
- **Systemabhängigkeiten:** (für PyQt6, FastAPI)
  - `pip` (für Python-Pakete)
  - Ein kompatibler Webserver (z. B. `uvicorn`)

---

## Installation

### 1. Repository klonen
```bash
git clone https://github.com/lpi-org/lpi-analyser.git
cd lpi-analyser

### 2. Virtuelle Umgebung erstellen
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

### 3. Abhängigkeiten installieren
pip install .[client]
pip install .[server]

### Client starten
python -m src.client.main

### Server starten
uvicorn src.server.app:app --reload --host 0.0.0.0 --port 5000
