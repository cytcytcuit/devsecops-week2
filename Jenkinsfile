pipeline {
    agent any

    stages {

        stage('Install Python') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip python3-venv
                '''
            }
        }

        stage('Build') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest
                '''
            }
        }

        stage('Security Scan') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install bandit
                    bandit -r src || true
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Simulating deployment to staging...'
            }
        }
    }
}
