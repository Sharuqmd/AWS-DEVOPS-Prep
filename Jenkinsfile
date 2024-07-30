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
                sh ''' $SCANNER_HOME/bin/sonar-scanner -Dsonar.url=http://3.7.71.223:9000/ -Dsonar.login=squ_797f44a87b9bde2fbb85f3d5029cd187866058e9
                        -Dsonar.projectName=medicare \
                        -Dsonar.java.binaries=. \
                        -Dsonar.projectKey=medicare '''
            }
        }
    }
}
