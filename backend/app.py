# backend/app.py
import os
from flask import Flask, render_template, request, jsonify
from backend.validators import validate_form

# Projektbasis bestimmen (ein Verzeichnis oberhalb von /backend)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 2) On construit les chemins absolus vers templates et static
TEMPLATES_DIR = os.path.join(BASE_DIR, 'frontend', 'templates')
STATIC_DIR    = os.path.join(BASE_DIR, 'frontend', 'static')

# Absolute Pfade für Templates und statische Dateien aufbauen
app = Flask(
    __name__,
    template_folder=TEMPLATES_DIR,
    static_folder=STATIC_DIR
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    data   = request.get_json()
    result = validate_form(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

