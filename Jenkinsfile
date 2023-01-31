pipeline {
    agent {
        label 'windows'
    }
    stages {
        stage('clone') {
            steps {
                git branch: "main",
                    credentialsId: 'dockerhub-credentials',
                    url: 'https://github.com/hoaduy994/weather-v1.git'
            }
        }

        stage('Install Python') {
            steps {
                bat 'choco install python --version 3.9.0'
            }
        }
        stage('Verify installation') {
            steps {
                bat 'python --version'
                bat 'python -m ensurepip --upgrade'
            }
        }
        
        stage('Install Python') {
            steps {
                sh 'sudo apt-get update'
                sh 'sudo apt-get install -y python3'
            }
        }
        stage('Install pip') {
            steps {
                sh 'sudo apt-get install -y python3-pip'
            }
        }
        stage('Verify installation') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
            }
        }

        stage('Install pip') {
            
            steps {
                script {
                    sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
                    sh 'python get-pip.py'
                }   
            }
        }

        stage('Setup') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('testing') {
            steps {
                sh 'python -m unittest discover'
            }

        }       
        
    }
}
