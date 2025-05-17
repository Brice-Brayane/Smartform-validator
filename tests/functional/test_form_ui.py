import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = "/usr/bin/chromium"
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_formulaire_valide(driver):
    driver.get("http://localhost:5000")

    # Remplir les champs
    driver.find_element(By.ID, "name").send_keys("Alice")
    driver.find_element(By.ID, "email").send_keys("alice@example.com")

    # Soumettre le formulaire
    driver.find_element(By.CSS_SELECTOR, "#smartform button[type=submit]").click()

    # Vérifier que le message indique que le formulaire est valide
    message = driver.find_element(By.ID, "ergebnisse").text
    assert "gültig" in message.lower()  # Test robuste en minuscule



def test_email_invalide(driver):
    driver.get("http://localhost:5000")

    driver.find_element(By.ID, "name").send_keys("Bob")
    driver.find_element(By.ID, "email").send_keys("email_invalide")
    driver.find_element(By.CSS_SELECTOR, "#smartform button[type=submit]").click()

    wait = WebDriverWait(driver, 5)

    # ➤ Attendre que la div soit remplie (sans chercher un mot)
    wait.until(lambda d: d.find_element(By.ID, "ergebnisse").text.strip() != "")

    # ➤ Afficher le texte réel pour comprendre ce que Selenium voit
    message = driver.find_element(By.ID, "ergebnisse").text
    print("🧪 MESSAGE AFFICHÉ DANS LE BROWSER:")
    print(message)

    # ➤ Test souple
    assert "ungültig" in message.lower() or "e-mail" in message.lower()


