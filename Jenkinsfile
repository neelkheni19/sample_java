pipeline {
    agent any

    tools {
        maven 'Maven3'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/neelkheni19 /sample_java.git'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn compile' // If on Windows: bat 'mvn compile'
            }
        }

        stage('Test') {
            steps {
                sh 'mvn test' // If on Windows: bat 'mvn test'
            }
        }
    }
}
