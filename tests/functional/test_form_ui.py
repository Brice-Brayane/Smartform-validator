# tests/functional/test_form_ui.py
# --------------------------------------------------------------------
# Funktionale UI-Tests für das SmartForm-Frontend mit Selenium.
# Ziel:
#   - Validierung der Benutzerinteraktion (Formularabsendung)
#   - Prüfung der Ausgabe von Fehler- bzw. Erfolgsmeldungen
#
# Hinweise:
#   - Erwartet einen laufenden Server unter base_url (siehe Fixture).
#   - Headless-Betrieb für CI-Umgebungen aktiviert.
#   - Explizite Waits (WebDriverWait) für robuste Synchronisation.
# --------------------------------------------------------------------

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="session")
def base_url() -> str:
    """
    Basis-URL der Anwendung.
    Bei Bedarf über Umgebungsvariable/CI anpassbar.
    """
    return "http://localhost:5000"


@pytest.fixture(scope="session")
def driver():
    """
    Initialisiert einen Firefox-WebDriver im Headless-Modus.
    Lebensdauer: gesamte Testsession.
    """
    options = Options()
    options.headless = True
    service = Service(executable_path=GeckoDriverManager().install())
    drv = webdriver.Firefox(service=service, options=options)
    # Optional: kleines Fenstermanagement für konsistente Layouts
    drv.set_window_size(1280, 900)
    yield drv
    drv.quit()


@pytest.fixture
def wait(driver):
    """
    Expliziter Wait für wiederverwendbare, stabile Synchronisation.
    """
    return WebDriverWait(driver, 5)  # Sekunden-Timeout


def test_empty_form_shows_errors(driver, wait, base_url):
    """
    Leeres Formular absenden -> Fehlermeldungen für 'name' und 'email' erwartet.
    """
    driver.get(base_url)

    # Formular absenden (ohne Eingaben)
    driver.find_element(By.CSS_SELECTOR, "form#smartform button[type='submit']").click()

    # Auf mindestens eine Fehlermeldung warten
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ergebnisse p")))

    # Alle Fehlermeldungen sammeln und in Kleinbuchstaben vergleichen
    errors = driver.find_elements(By.CSS_SELECTOR, "#ergebnisse p")
    texts = [e.text.lower() for e in errors]

    assert any("name" in t for t in texts), "Fehlermeldung für 'name' fehlt."
    assert any("email" in t for t in texts), "Fehlermeldung für 'email' fehlt."


def test_valid_form_shows_success(driver, wait, base_url):
    """
    Gültige Eingaben absenden -> Erfolgsmeldung erwartet.
    """
    driver.get(base_url)

    # Felder befüllen
    driver.find_element(By.ID, "name").send_keys("TestUser")
    driver.find_element(By.ID, "email").send_keys("test@example.com")

    # Formular absenden
    driver.find_element(By.CSS_SELECTOR, "form#smartform button[type='submit']").click()

    # Auf Erfolgsmeldung warten
    success = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ergebnisse p")))
    assert "gültig" in success.text.lower(), "Erfolgsmeldung wurde nicht angezeigt."
