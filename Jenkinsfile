pipeline {
    agent any

    environment {
        SONAR_HOST_URL = 'http://10.255.255.254:9000'
        SONAR_LOGIN = credentials('sonarqube-token')
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'develop',
                    url: 'https://github.com/yulianiandrea12/crud_django_usuarios.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Pruebas Unitarias') {
            steps {
                sh '''
                . venv/bin/activate
                python3 manage.py test
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('MySonarQube') {
                    sh '''
                    sonar-scanner \
                        -Dsonar.projectKey=crud_django \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=$SONAR_HOST_URL \
                        -Dsonar.login=$SONAR_LOGIN
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 3, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
