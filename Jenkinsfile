pipeline{
    environment {
        registry = 'hoaduy994/weather-v1'
        registryCredential = 'dockerhub-credentials'
        dockerImage = ''
        build_version = "1+${BUILD_NUMBER}"
    }
    agent any

    stages {
        stage('Clone github repo'){
            steps {
                git credentialsId: 'github-credentials', url: 'https://github.com/hoaduy994/weather-v1.git', branch: 'main'
            }
        }

        stage('Setup') {
            steps {
                sh 'pip install -r requirements.txt --user'
            }
        }

        stage('testing') {
            steps {
                sh 'python -m unittest discover'
            }

        }       
        
    }
}
