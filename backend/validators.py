# backend/validators.py
# ---------------------------------------------------------------
# Enthält Validierungsfunktionen für das SmartForm-Projekt.
# Alle Kommentare auf Deutsch.
# ---------------------------------------------------------------

import re
from backend.forms import FormData   # import absolu

def is_valid_email(email: str) -> bool:
    """
    Prüft mit einem einfachen Regex, ob die E-Mail-Adresse gültig ist.
    Rückgabe: True, wenn gültig, sonst False.
    """
    pattern = r'^\S+@\S+\.\S+$'
    return re.match(pattern, email) is not None

def validate_form(data):
    """
    Hauptfunktion zur Formular-Validierung.
    Nimmt ein Dictionary (z. B. von request.get_json()) entgegen und
    gibt ein Ergebnisobjekt mit 'valid' und 'errors' zurück.
    """
    form = FormData(data)
    errors = {}

    # Regel 1: Name ist Pflichtfeld
    if not form.get('name'):
        errors['name'] = 'Name ist erforderlich.'

    # Regel 2: E-Mail muss gültig sein
    email = form.get('email')
    if not is_valid_email(email):
        errors['email'] = 'Ungültige E-Mail-Adresse.'

    return {
        'valid': len(errors) == 0,
        'errors': errors
    }
