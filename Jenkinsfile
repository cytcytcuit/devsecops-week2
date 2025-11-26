pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Security Scan') {
            steps {
                sh 'bandit -r src || true'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Simulating deployment to staging server...'
            }
        }
    }
}
