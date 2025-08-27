# Dockerfile
# --------------------------------------------------------------------
# SmartForm: Container-Image für Backend (Flask)
# Ziele:
#  - Schlankes, reproduzierbares Python-Image (3.11-slim)
#  - Systemabhängigkeiten nur falls benötigt (z. B. für psycopg2)
#  - Keine Bytecode-/Buffer-Artefakte in Logs
#  - Non-Root-Betrieb für bessere Sicherheit
#  - Trennung von Build- und Runtime-Schritten (Layer-Effizienz)
# --------------------------------------------------------------------

FROM python:3.11-slim AS base

# Systemweite Grundeinstellungen
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    # Optional: Flask-Kontext (kann per Compose/.env überschrieben werden)
    FLASK_ENV=production \
    # Standard-Port der App (siehe EXPOSE unten)
    APP_PORT=5000

# Verzeichnis für App-Code
WORKDIR /app

# Benötigte Systempakete:
#  - build-essential, gcc: nur nötig, wenn wheels gebaut werden (z. B. psycopg2)
#  - curl: für Healthchecks/Debug (optional)
#  - libpq-dev: Header für PostgreSQL-Client (psycopg2)
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
      build-essential gcc \
      libpq-dev \
      curl \
    && rm -rf /var/lib/apt/lists/*

# Nur requirements zuerst kopieren (bessere Layer-Caches)
COPY backend/requirements.txt ./requirements.txt

# Abhängigkeiten installieren
RUN pip install -r requirements.txt

# App-Code kopieren (nachdem Dependencies gecacht wurden)
COPY . .

# Non-Root-User anlegen und Rechte setzen
RUN useradd --create-home --shell /bin/bash appuser && \
    chown -R appuser:appuser /app
USER appuser

# Port deklarieren (informativ; Mapping erfolgt durch Compose/Orchestrator)
EXPOSE 5000

# ------------------------------------------------------------
# Startkommando:
# 1) Entwicklung: Flask-Dev-Server (nicht für Produktion)
# 2) Produktion: Gunicorn (empfohlen), siehe Kommentar
# ------------------------------------------------------------

# Entwicklung (einfach):
# CMD ["python", "-m", "backend.app"]

# Produktion (empfohlen): Gunicorn als WSGI-Server
# - workers: 2–4 für kleine Container
# - bind: an alle Interfaces auf APP_PORT
# - module: backend.app:app (WSGI-Application)
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "backend.app:app"]
