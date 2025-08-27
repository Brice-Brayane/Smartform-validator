# SmartForm Validator

SmartForm Validator ist ein Demonstrationsprojekt für moderne **Software-Qualitätssicherung** mit Fokus auf **Testautomatisierung** und **CI/CD**.  
Die Anwendung zeigt, wie eine kleine Web-App (Flask + JavaScript) durch systematische Tests, Dockerisierung und Jenkins-Pipelines stabil und reproduzierbar entwickelt werden kann.

---

## Ziele des Projekts

- Aufbau einer vollständigen **Testpyramide**:
  - Unit-Tests für Validierungslogik (PyTest)
  - Funktionale UI-Tests mit Selenium (Headless Browser)
- Integration von **Testmanagement** und strukturierter Fehlerdokumentation
- Reproduzierbare Infrastruktur mit **Docker & Docker Compose**
- Automatisierte Pipeline mit **Jenkins** (Build → Test → Reports → Cleanup)
- Erweiterbarkeit für den Einsatz in regulierten oder hochverfügbaren Umgebungen

---

## Projektstruktur

├── backend/ # Flask-Backend (App, Validierung, Business-Logik)
│ ├── app.py
│ ├── forms.py
│ ├── validators.py
│ └── requirements.txt
├── frontend/ # Statisches Frontend (HTML + JS)
│ ├── static/
│ │ └── script.js
│ └── templates/
│ └── index.html
├── tests/ # Test-Suite (Unit + Functional)
│ ├── unit/
│ │ └── test_validators.py
│ └── functional/
│ └── test_form_ui.py
├── docker-compose.yml # Services (App + PostgreSQL)
├── Dockerfile # Backend-Image (Python + Flask)
├── Jenkinsfile # CI/CD-Pipeline
└── README.md # Projektdokumentation



---

## Installation & Start

### Voraussetzungen
- Docker & Docker Compose
- Python 3.11 (optional, für lokalen Lauf ohne Docker)
- Firefox/GeckoDriver (für Selenium-Tests lokal)

### Start mit Docker Compose
```bash
git clone https://github.com/Brice-Brayane/Smartform-validator.git
cd Smartform-validator
docker compose up --build



Die Anwendung ist erreichbar unter:
http://localhost:5000




## Tests
Unit-Tests
docker compose exec app pytest tests/unit -v

Funktionale Tests (UI mit Selenium)
docker compose exec app pytest tests/functional -v

Alle Tests mit Coverage & JUnit-Report
docker compose exec app pytest tests --cov=backend --junitxml=test-results/junit.xml



## CI/CD Pipeline (Jenkins)

Die Pipeline (Jenkinsfile) umfasst:

Checkout aus dem Git-Repository

Build des Docker-Images

Start von App + Datenbank (inkl. Healthcheck)

Testausführung (Unit + Functional)

Archivierung von Testergebnissen (JUnit, Coverage)

Automatisches Aufräumen der Services


## Tech-Stack

Backend: Python 3.11, Flask

Frontend: HTML, Vanilla JavaScript

Datenbank: PostgreSQL 15

Testautomatisierung: PyTest, Selenium, WebDriverManager

CI/CD: Jenkins, Docker, GitHub Actions (optional integrierbar)


## Qualitätsaspekte

Kommentierter, klar strukturierter Code (deutschsprachige Docstrings und Kommentare, unternehmensüblich)

Trennung von Unit- und Functional-Tests → schnellere Feedbackzyklen

Reproduzierbare Containerumgebung für Dev & CI

Non-Root-User im Docker-Image


## Erweiterbar für:

zusätzliche Validierungsregeln

Integration in Jira-Testmanagement

Reporting mit Allure oder pytest-html
