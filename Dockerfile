# Basis-Image
FROM python:3.13-slim

# Arbeitsverzeichnis im Container festlegen
WORKDIR /app

# Abhängigkeiten kopieren und installieren
COPY pyproject.toml LICENSE.txt README.md /app/
RUN ls -la /app && pip install --upgrade pip setuptools wheel && pip install .

# Quellcode kopieren
COPY src /app/src

# Umgebungsvariablen setzen (optional)
ENV PYTHONUNBUFFERED=1

# Startbefehl
CMD ["python", "src/main.py"]
