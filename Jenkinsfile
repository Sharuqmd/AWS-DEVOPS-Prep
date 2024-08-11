pipeline {
    agent any
    tools {
        maven 'm3' 
    }
    environment {
        SCANNER_HOME = tool 'sonar-scanner'
        SONAR_URL = 'http://13.234.117.197:9000'
        SONAR_LOGIN = 'squ_e050f380d01fb9894a75057b18ff484e48d0dd99'
        SONAR_PROJECT_NAME = 'medicare'
        SONAR_PROJECT_KEY = 'medicare'
        DOCKER_CREDENTIALS_ID = 'docker'
        AWS_CREDENTIALS_ID = 'aws'
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
              withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: AWS_CREDENTIALS_ID]]) {
                script {
                    sh '''
                    terraform workspace select test || terraform workspace new test
                    terraform init
                    terraform destroy -auto-approve
                    '''
                }
              }
            }
        }
        stage('Configure kubectl') {
            steps {
              withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: AWS_CREDENTIALS_ID]]) {
                script {
                    sh '''
                    aws eks update-kubeconfig --name eks-my-cluster --region ap-south-1
                    '''
                    sh '''
                    kubectl apply -f k8.yaml
                    '''
                }
              }
            }
        }
        stage('Selenium test') {
            steps {
              sh "python -m venv my-venv"
              sh "my-venv/bin/pip install selenium"
              sh "source my-env/bin/activate"
              sh "docker run -d -p 4444:4444 selenium/standalone-chrome"
              sh "python3 test.py"
            }
        }
    }
}
