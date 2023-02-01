pipeline {
    agent any 
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t hoady994/jenkins .'
            }
        }
        stage('Login') {
            steps {
                sh 'echo $dckr_pat_qceJuj3b7Lb5vwUmpBnANtecqwk | docker login -u $jenkins --password-stdin'
            }
        }
        stage('Push') {
            steps {
                sh 'docker push hoady994/jenkins'
            }
        }
        // stage('clone') {
        //     steps {
        //         git branch: "main",
        //             credentialsId: 'dockerhub-credentials',
        //             url: 'https://github.com/hoaduy994/weather-v1.git'
        //     }
        // }

        // stage('Install pip') {
            
        //     steps {
        //         script {
        //             sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
        //             sh 'python get-pip.py'
        //         }   
        //     }
        // }

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
    post {
        always {
            sh 'docker logout'
        }
    }
}
