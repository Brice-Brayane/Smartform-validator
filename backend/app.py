# backend/app.py
import os
from flask import Flask, render_template, request, jsonify
from backend.validators import validate_form

# Projektbasis bestimmen (ein Verzeichnis oberhalb von /backend)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Absolute Pfade für Templates und statische Dateien aufbauen
TEMPLATES_DIR = os.path.join(BASE_DIR, 'frontend', 'templates')
STATIC_DIR    = os.path.join(BASE_DIR, 'frontend', 'static')

# Flask-App initialisieren und Pfade für Templates/Static setzen
app = Flask(
    __name__,
    template_folder=TEMPLATES_DIR,
    static_folder=STATIC_DIR
)

@app.route('/')
def index():
    # Startseite rendern (Frontend: index.html)
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    # Formulardaten aus dem Request laden
    data = request.get_json()
    # Validierung der Daten über eigene Funktion
    result = validate_form(data)
    # Ergebnis als JSON-Response zurückgeben
    return jsonify(result)

if __name__ == '__main__':
    # Lokalen Server starten (0.0.0.0 = von außen erreichbar, Port 5000)
    # Debug=True nur für Entwicklung, nicht für Produktion empfohlen
    app.run(host='0.0.0.0', port=5000, debug=True)
