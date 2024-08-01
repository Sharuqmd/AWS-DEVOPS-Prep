pipeline {
    agent any
    tools {
        maven 'm3' 
    }
    environment {
        SCANNER_HOME = tool 'sonar-scanner'
        SONAR_URL = 'http://35.154.166.14:9000'
        SONAR_LOGIN = 'squ_1a17645e256d0cf2cf3c0ec735cb4de0066be870'
        SONAR_PROJECT_NAME = 'medicare'
        SONAR_PROJECT_KEY = 'medicare'
        DOCKER_CREDENTIALS_ID = 'docker'
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
        stage('Build') {
            steps {
                sh 'mvn clean install'
            }
        } 
        stage('Build and push Docker image') {
            steps {
               script {
                  docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDENTIALS_ID)   {
                      sh 'docker build -t medicareapp .'
                      sh 'docker tag medicareapp sharuq/medicare:latest'
                      sh 'docker push sharuq/medicare:latest'
}
               }
            }
        }
        stage('Running application') {
            steps {
                sh 'docker run -d -p 9092:8082 --name=app sharuq/medicare:latest '
            }
        }          
    }
}
