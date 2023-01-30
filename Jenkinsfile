pipeline{
    environment {
        registry = 'hoaduy994/weather-v1'

    }
    agent any

    stages {
        stage('Clone'){
            steps {
                git 'https://github.com/hoaduy994/weather-v1.git'
            }
        }

        stage('Setup') {
            steps {
                sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('testing') {
            steps {
                sh 'python -m unittest discover'
            }

        }       
        
    }
}
