pipeline {
    agent any

   environment {
    PYTHON_HOME = "C:\\Users\\Neel Kheni\\AppData\\Local\\Microsoft\\WindowsApps"
    PATH = "${env.PYTHON_HOME};${env.PYTHON_HOME}\\Scripts;${env.PATH}"
 }


    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/neelkheni19/sample_java.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install --upgrade pip'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m unittest discover -s . -p "test_*.py"'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Some tests failed!'
        }
    }
}
