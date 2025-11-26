pipeline {
    agent any

    stages {

        stage('Install Python') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip
                '''
            }
        }

        stage('Build') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Security Scan') {
            steps {
                sh '''
                    pip3 install bandit
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
