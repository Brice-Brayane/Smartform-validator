# backend/forms.py
# ---------------------------------------------------------------
# Repräsentiert die Formulardaten und bietet Zugriff über .get()
# ---------------------------------------------------------------

class FormData:
    """
    Repräsentation der Formulardaten.
    Ermöglicht einen sauberen Zugriff auf Felder via .get().
    """

    def __init__(self, data):
        self.data = data

    def get(self, field_name):
        return self.data.get(field_name, None)
