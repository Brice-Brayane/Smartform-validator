// Jenkinsfile
// ---------------------------------------------------------------
// Automatisiertes CI/CD-Pipeline-Skript für SmartForm Validator
// Alle Kommentare auf Deutsch.
// ---------------------------------------------------------------

pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = 'smartform-validator'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Brice-Brayane/Smartform-validator.git' 
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Start Services') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker compose exec app pytest /app/tests --maxfail=1 -q || true'
            }
        }

        stage('Stop Services') {
            steps {
                sh 'docker compose down'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/test-results/**/*.xml', allowEmptyArchive: true
            junit '**/test-results/**/*.xml'
        }
    }
}
