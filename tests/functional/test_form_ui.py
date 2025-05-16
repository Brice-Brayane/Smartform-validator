# tests/functional/test_form_ui.py
# ---------------------------------------------------------------
# Selenium-Test für das SmartForm-Formular (Headless Firefox).
# ---------------------------------------------------------------

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.headless = True
    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()

def test_empty_form_shows_errors(driver):
    driver.get("http://localhost:5000")
    driver.find_element(By.XPATH, "//button[text()='Validieren']").click()
    errors = driver.find_elements(By.CSS_SELECTOR, "#ergebnisse p")
    texts = [e.text.lower() for e in errors]
    assert any("name" in t for t in texts)
    assert any("email" in t for t in texts)

def test_valid_form_shows_success(driver):
    driver.get("http://localhost:5000")
    driver.find_element(By.ID, "name").send_keys("TestUser")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.XPATH, "//button[text()='Validieren']").click()
    success = driver.find_element(By.CSS_SELECTOR, "#ergebnisse p")
    assert "gültig" in success.text.lower()
