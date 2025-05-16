// Jenkinsfile
// ---------------------------------------------------------------
// Automatisiertes CI/CD-Pipeline-Skript für SmartForm Validator
// Alle Kommentare auf Deutsch.
// ---------------------------------------------------------------

pipeline {
    agent any

    stages {
        stage('Quellcode klonen') {
            steps {
                // Repository klonen
                git 'https://github.com/votre-utilisateur/smartform-validator.git'
            }
        }

        stage('Docker-Image bauen') {
            steps {
                sh 'docker compose build --no-cache app'
            }
        }

        stage('Unit-Tests ausführen') {
            steps {
                sh 'docker compose up -d db'
                sh 'docker compose run --rm app pytest tests/unit -q'
            }
        }

        stage('Functional-Tests (Selenium)') {
            steps {
                sh 'docker compose up -d'
                sh 'docker compose exec app pytest tests/functional -q'
            }
        }

        stage('Deployment') {
            steps {
                // Beispiel: in Produktions-Umgebung deployen
                // sh 'ansible-playbook -i inventory deploy.yml'
                echo 'Deployment-Schritte hier einfügen'
            }
        }
    }
}
