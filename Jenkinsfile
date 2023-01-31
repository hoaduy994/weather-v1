pipeline {
    agent none

    stages {
        // stage('Clone github repo'){
        //     steps {
        //         git 'https://github.com/hoaduy994/weather-v1.git'
        //     }
        // }

        stage('Install pip') {
            agent {
                docker {
                    image 'python:3.11.1'
                }
            }
            steps {
                    sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
                    sh 'python get-pip.py'
                    // sh 'python --version'    
            }
        }

        stage('Setup') { // Install any dependencies you need to perform testing
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
