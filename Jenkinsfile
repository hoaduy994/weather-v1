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
                script{
                    sh """
                    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                    /path/to/python get-pip.py
                    """
                }
                
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
