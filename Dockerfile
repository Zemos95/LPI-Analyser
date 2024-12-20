# Basis-Image
FROM python:3.13-slim

# Arbeitsverzeichnis erstellen
WORKDIR /app

# Abhängigkeiten kopieren und installieren
COPY pyproject.toml /app/
RUN pip install --upgrade pip && pip install hatch && hatch env create

# Quellcode kopieren
COPY src /app/src

# Umgebungsvariablen setzen (optional)
ENV PYTHONUNBUFFERED=1

# Startkommando für die Anwendung
CMD ["hatch", "run", "python", "src/main.py"]
