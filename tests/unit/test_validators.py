# tests/unit/test_validators.py
# ---------------------------------------------------------------
# Unit-Tests für die Validierungslogik
# ---------------------------------------------------------------

import pytest
from backend.validators import is_valid_email, validate_form

@pytest.mark.parametrize(
    "email, erwartet",
    [
        ("test@example.com", True),
        ("user.name+tag@sub.domain.de", True),
        ("kein-at-symbol.de", False),
        ("@keineadresse", False),
    ],
)
def test_is_valid_email(email, erwartet):
    assert is_valid_email(email) is erwartet

def test_validate_form_ok():
    payload = {"name": "Anna", "email": "anna@example.com"}
    result = validate_form(payload)
    assert result["valid"] is True
    assert result["errors"] == {}

def test_validate_form_fehler():
    payload = {"name": "", "email": "falsch@"}
    result = validate_form(payload)
    assert result["valid"] is False
    assert "name" in result["errors"]
    assert "email" in result["errors"]
