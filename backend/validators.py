# backend/validators.py
# --------------------------------------------------------------------
# Validierungsfunktionen für das SmartForm-Projekt.
# Enthält Prüfungen für Pflichtfelder und E-Mail-Format.
# --------------------------------------------------------------------

import re
from backend.forms import FormData   # Import der FormData-Klasse

def is_valid_email(email: str) -> bool:
    """
    Prüft, ob eine E-Mail-Adresse formal gültig ist.
    
    - Verwendet einen einfachen Regex.
    - Rückgabe: True, wenn Format korrekt, sonst False.

    Hinweis:
    Dies ist eine Basisprüfung (Syntax). Für produktive Systeme
    wären erweiterte Checks erforderlich (z. B. MX-Records).
    """
    pattern = r'^\S+@\S+\.\S+$'
    return re.match(pattern, email) is not None


def validate_form(data: dict) -> dict:
    """
    Hauptfunktion zur Validierung von Formulardaten.

    Parameter:
        data (dict): Eingabedaten, typischerweise von request.get_json()

    Ablauf:
        1. Erzeugt ein FormData-Objekt.
        2. Führt Validierungsregeln aus (Pflichtfelder, E-Mail).
        3. Sammelt alle Fehler in einem Dictionary.

    Rückgabe:
        dict: {
            'valid': bool,   # True, wenn alle Regeln erfüllt
            'errors': dict   # Feldname -> Fehlermeldung
        }
    """
    form = FormData(data)
    errors = {}

    # Regel 1: Name darf nicht leer sein
    if not form.get('name'):
        errors['name'] = 'Name ist erforderlich.'

    # Regel 2: E-Mail muss existieren und gültig sein
    email = form.get('email')
    if not email or not is_valid_email(email):
        errors['email'] = 'Ungültige E-Mail-Adresse.'

    return {
        'valid': len(errors) == 0,
        'errors': errors
    }
