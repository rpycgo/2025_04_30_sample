pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Test for PR to develop') {
            when {
                allOf {
                    expression { return env.CHANGE_TARGET == 'develop' }
                    expression { return env.CHANGE_ID != null }  // 실제 PR인 경우만
                }
            }
            steps {
                echo "Running test.py for PR to develop branch..."
                sh 'python3 test.py'
            }
        }

        stage('Run Test for other cases') {
            when {
                expression { return env.BRANCH_NAME == 'develop' && env.CHANGE_ID == null }
            }
            steps {
                echo "Running test.py for regular push to develop"
                sh 'python3 test.py'
            }
        }
    }
}