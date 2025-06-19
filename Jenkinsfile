pipeline {
    agent any

    triggers {
        githubPullRequest()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run only on develop PRs') {
            when {
                expression {
                    return env.ghprbTargetBranch == 'develop'
                }
            }
            steps {
                echo "Pull request into develop detected."
                sh 'python3 test.py'
            }
        }
    }
}
