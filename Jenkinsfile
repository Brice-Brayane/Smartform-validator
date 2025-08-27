// Jenkinsfile
// --------------------------------------------------------------------
// CI/CD-Pipeline für das SmartForm-Projekt (Docker Compose + PyTest)
// Ziele:
//  - Reproduzierbarer Build der Container
//  - Start der Services und Health-Check der App
//  - Ausführung von Unit-/Functional-Tests mit JUnit-Report
//  - Archivierung von Testergebnissen und optional Coverage
// --------------------------------------------------------------------

pipeline {
  agent any

  options {
    timestamps()                    // Zeitstempel in der Console-Log
    ansiColor('xterm')              // Farbausgabe für bessere Lesbarkeit
    disableConcurrentBuilds()       // Keine parallelen Builds desselben Jobs
  }

  parameters {
    string(name: 'REPO_URL',   defaultValue: 'https://github.com/Brice-Brayane/Smartform-validator.git', description: 'Git-Repository (https/ssh)')
    string(name: 'BRANCH',     defaultValue: 'main', description: 'Branch/Ref zum Auschecken')
    string(name: 'BASE_URL',   defaultValue: 'http://localhost:5000', description: 'Basis-URL der laufenden App für UI-Tests')
  }

  environment {
    COMPOSE_PROJECT_NAME = 'smartform-validator'
    APP_SERVICE          = 'app'                // Name des App-Services in docker-compose.yml
    TEST_RESULTS_DIR     = 'test-results'       // JUnit-Zielfolder (wird archiviert)
    COVERAGE_DIR         = 'htmlcov'            // optional: Coverage-HTML (pytest-cov notwendig)
  }

  stages {

    stage('Checkout') {
      steps {
        // Repository und Ziel-Branch aus Parametern
        git branch: params.BRANCH, url: params.REPO_URL
      }
    }

    stage('Build') {
      steps {
        sh 'docker compose version'
        sh 'docker compose build --pull'
      }
    }

    stage('Start Services') {
      steps {
        // Services im Hintergrund starten
        sh 'docker compose up -d'

        // Health-/Readiness-Check der App (falls kein HEALTHCHECK definiert)
        // Wartet bis HTTP 200/OK erreichbar ist.
        sh '''
          echo "Warte auf Applikation unter ${BASE_URL} ..."
          for i in {1..60}; do
            if curl -fsS "${BASE_URL}" >/dev/null 2>&1; then
              echo "Applikation ist erreichbar."
              exit 0
            fi
            sleep 2
          done
          echo "Applikation nicht erreichbar."
          exit 1
        '''
      }
    }

    stage('Tests') {
      steps {
        // Sicherstellen, dass Ergebnisverzeichnisse existieren
        sh '''
          mkdir -p ${TEST_RESULTS_DIR}
          # Tests innerhalb des App-Containers ausführen
          # JUnit-XML erzeugen; optional Coverage (falls pytest-cov installiert)
          docker compose exec -T ${APP_SERVICE} \
            sh -lc "pytest tests \
              --junitxml=/app/${TEST_RESULTS_DIR}/junit.xml \
              -q"
        '''
      }
      post {
        always {
          // JUnit-Reports einsammeln (Stage-Fail bleibt sichtbar)
          junit allowEmptyResults: true, testResults: "${TEST_RESULTS_DIR}/junit.xml"
          // Optional: Coverage-HTML archivieren, falls vorhanden
          script {
            if (fileExists("${COVERAGE_DIR}/index.html")) {
              archiveArtifacts artifacts: "${COVERAGE_DIR}/**", allowEmptyArchive: true
            }
          }
          // Auch Roh-Artefakte aus dem Container holen (falls nötig):
          // sh "docker cp $(docker compose ps -q ${APP_SERVICE}):/app/${TEST_RESULTS_DIR} ./"
          archiveArtifacts artifacts: "${TEST_RESULTS_DIR}/**", allowEmptyArchive: true
        }
      }
    }
  }

  post {
    always {
      // Services und Volumes sauber beenden/aufräumen
      sh 'docker compose down -v'
    }
    success {
      echo 'Build und Tests erfolgreich abgeschlossen.'
    }
    failure {
      echo 'Build/Tests fehlgeschlagen. Bitte Console-Log und JUnit-Report prüfen.'
    }
  }
}
