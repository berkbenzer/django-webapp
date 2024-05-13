pipeline {
    agent any

    stages {
        stage("Build Docker Image") {
            steps {
                script {
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/berkbenzer/django-webapp.git']])
                    sh "docker build --tag python-django:latest ."
                }
                sh "docker tag python-django:latest <<USERNAME>>/python-django:latest"
            }
        }
        stage("Push Docker Image to Docker Hub") {
            steps {
                script {
                    withCredentials([string(credentialsId: 'dockerhubpasswd', variable: 'dockerhubpasswd')]) { 
                        sh "docker login -u <<USERNAME>> -p ${dockerhubpasswd}"
                    }
                    sh "docker push <<USERNAME>>/python-django:latest"
                }
            }
        }
    }
}
