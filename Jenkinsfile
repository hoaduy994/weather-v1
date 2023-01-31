pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/scripts/activate'
                sh 'pip install python-jenkins'
            }
        }

        // stage('Install pip') {
            
        //     steps {
        //             sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
        //             sh 'python get-pip.py'
        //             // sh 'python --version'    
        //     }
        // }

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
