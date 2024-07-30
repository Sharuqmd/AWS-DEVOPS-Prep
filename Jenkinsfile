pipeline {
    agent any
    tools{
        
        maven 'm3'
    }
    environment{
        SCANNER_HOME= tool 'sonar-scanner'
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
                sh ''' $SCANNER_HOME/bin/sonar-scanner -Dsonar.url=http://3.7.71.223:9000/ -Dsonar.login=sqp_0f3407702cdad9649a9ff890d62d8f3ba93db1c0 -Dsonar.projectName=medicare \
                        -Dsonar.java.binaries=. \
                        -Dsonar.projectKey=medicare '''
            }
        }
    }
}
