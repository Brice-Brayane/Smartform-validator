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
