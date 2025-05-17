# backend/forms.py

class FormData:
    def __init__(self, data):
        self.data = data

    def get(self, field_name, default=None):
        value = self.data.get(field_name, default)
        return value.strip() if isinstance(value, str) else value

    def get_int(self, field_name, default=0):
        try:
            return int(self.get(field_name))
        except (ValueError, TypeError):
            return default
