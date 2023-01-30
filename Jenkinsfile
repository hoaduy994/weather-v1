pipeline{
    agent any

    stages {
        stage('Clone github repo'){
            steps {
                git 'https://github.com/hoaduy994/weather-v1.git'
            }
        }
        stage('checkmap'){
            steps {
                sh 'pip --version'
            }
        }
        // stage('Setup') {
        //     steps {
        //         sh 'pip install -r requirements.txt'
        //     }
        // }

        // stage('testing') {
        //     steps {
        //         sh 'python -m unittest discover'
        //     }

        // }       
        
    }
}
