# Basis-Image
FROM python:3.13-slim

# Installiere notwendige Systembibliotheken für PyQt6 und X11-Unterstützung
RUN apt-get update && apt-get install -y \
    libgl1-mesa-dri \
    libgl1-mesa-glx \
    libegl1-mesa \
    libxrender1 \
    libxext6 \
    libxkbcommon0 \
    libfontconfig1 \
    libfreetype6 \
    libxi6 \
    libxrandr2 \
    libxcb1 \
    libxcb-util1 \
    libx11-6 \
    libglib2.0-0 \
    libdbus-1-3 \
    libxcb-cursor0 \
    libxcb-render0 \
    libxcb-shape0 \
    libxcb-shm0 \
    libxcb-xfixes0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-xinerama0 \
    libxcb-sync1 \
    x11-utils \
    qtbase5-dev \
    && rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis im Container festlegen
WORKDIR /app

# Abhängigkeiten kopieren und installieren
COPY pyproject.toml LICENSE.txt README.md /app/
RUN ls -la /app && pip install --upgrade pip setuptools wheel && pip install .

# Quellcode kopieren
COPY src /app/src

# Umgebungsvariablen für X11 setzen
ENV QT_QPA_PLATFORM=xcb 
ENV QT_DEBUG_PLUGINS=1

# Start der Anwendung
CMD ["python", "src/main.py"]
