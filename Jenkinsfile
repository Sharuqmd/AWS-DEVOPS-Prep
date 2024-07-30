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
                sh ''' $SCANNER_HOME/bin/sonar-scanner -Dsonar.url=http://3.7.71.223:9000/ -Dsonar.login=squ_4851e413cfe0c323c4be9cf84c94ff360c1e9132
                        -Dsonar.projectName=medicare \
                        -Dsonar.java.binaries=. \
                        -Dsonar.projectKey=medicare '''
            }
        }
    }
}
