pipeline{
    agent any

    stages {
        stage('Clone github repo'){
            steps {
                git 'https://github.com/hoaduy994/weather-v1.git'
            }
        }

        stage('Install pip') {
            steps {
                    // sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
                    // sh 'python get-pip.py'
                    sh 'python --version'    
            }
        }

        stage('Setup') { // Install any dependencies you need to perform testing
            steps {
                script {
                    sh """
                    pip install -r requirements.txt
                    """
                }
            }
        }

        stage('testing') {
            steps {
                script {
                    sh """
                    python -m unittest discover
                    """
                }
            }

        }       
        
    }
}
