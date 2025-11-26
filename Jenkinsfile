pipeline {
    agent {
        docker {
            image 'python:3.10'
            args '-u root'
        }
    }

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
                sh 'pip install bandit && bandit -r src || true'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Simulating deployment to staging server...'
            }
        }
    }
}
