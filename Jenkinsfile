pipeline {
    agent any
    tools {
        maven 'm3' 
    }
    environment {
        SCANNER_HOME = tool 'sonar-scanner'
        SONAR_URL = 'http://65.2.37.199:9000/'
        SONAR_LOGIN = 'squ_ed23f27de91c4c4ed2af4ef532f6819f866793ed'
        SONAR_PROJECT_NAME = 'medicare'
        SONAR_PROJECT_KEY = 'medicare'
    }
    stages {
        stage('checkout') {
            steps {
                git 'https://github.com/Sharuqmd/Healthcare-project.git' 
            }
        }
        stage('compile') {
            steps {
                sh 'mvn clean compile'
            }
        }
        stage('sonar-analysis') {
            steps {
                sh '''${SCANNER_HOME}/bin/sonar-scanner \
                    -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                    -Dsonar.sources=. \
                    -Dsonar.java.binaries=. \
                    -Dsonar.projectName=${SONAR_PROJECT_NAME} \
                    -Dsonar.host.url=${SONAR_URL} \
                    -Dsonar.login=${SONAR_LOGIN}'''
            }
        }
    }
}
