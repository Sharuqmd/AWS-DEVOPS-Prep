pipeline {
    agent any
    tools {
        maven 'm3' 
    }
    environment {
        SCANNER_HOME = tool 'sonar-scanner'
        SONAR_URL = 'http://13.235.42.163:9000'
        SONAR_LOGIN = 'squ_13faeb4cabd7040448633d6feee6f5d397295263'
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
        stage('Terraform Apply') {
            steps {
                script {
                    sh '''
                    terraform init
                    terraform apply -auto-approve
                    '''
                }
            }
        }
        stage('Configure kubectl') {
            steps {
                script {
                    // Configure kubectl to use the EKS cluster
                    sh '''
                    aws eks update-kubeconfig --name eks-my-cluster --region ap-south-1
                    '''
                }
            }
        }
    }
}
