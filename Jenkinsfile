pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Check Python') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Run Test') {
            steps {
                sh 'python3 test.py'
            }
        }
    }
}
