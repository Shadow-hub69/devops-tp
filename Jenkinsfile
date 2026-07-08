pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t app-devops .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop app-devops-container || true'
                sh 'docker rm app-devops-container || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d --name app-devops-container -p 8080:80 app-devops'
            }
        }

    }
}
