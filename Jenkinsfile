pipeline {
    agent  any
    stages {
        stage('clone') {
            steps {
                git branch: "main",
                    credentialsId: 'dockerhub-credentials',
                    url: 'https://github.com/hoaduy994/weather-v1.git'
                sh 'python --version'
            }
        }
        stage('build') {
            steps {
                script {
                    sh """
                        python -m venv venv
                        . venv/scripts/activate
                        pip install python-jenkins
                    """
                }
            }
        }

        stage('Install pip') {
            
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
