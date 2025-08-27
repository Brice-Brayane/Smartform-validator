# backend/forms.py
# --------------------------------------------------------------------
# FormData-Klasse
# Zweck: Einheitliche Repräsentation von Formulardaten
#        und zentraler Zugriff über .get()
# --------------------------------------------------------------------

class FormData:
    """
    Repräsentiert strukturierte Formulardaten.

    Vorteile:
    - Einheitlicher Zugriff auf Eingabefelder über .get()
    - Vermeidung direkter Dictionary-Zugriffe
    - Ermöglicht spätere Erweiterungen (z. B. Validierung, Defaults)

    Parameter:
        data (dict): Eingabedaten (z. B. aus einem Request-Body)

    Methoden:
        get(field_name):
            Gibt den Wert eines Feldes zurück oder None, wenn das Feld fehlt.
    """

    def __init__(self, data):
        # Eingabedaten speichern (z. B. JSON-Daten aus Request)
        self.data = data

    def get(self, field_name):
        # Sicheren Zugriff auf ein Feld ermöglichen.
        # Gibt None zurück, falls das Feld nicht existiert.
        return self.data.get(field_name, None)
