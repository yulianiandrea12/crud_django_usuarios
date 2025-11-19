pipeline {
    agent any

    environment {
        SONARQUBE_URL = "http://10.255.255.254:9000"
        SONARQUBE_TOKEN = credentials('sonarqube-token')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'develop', url: 'https://github.com/yulianiandrea12/crud_django_usuarios.git'
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
                sh '''
                . venv/bin/activate
                sonar-scanner \
                  -Dsonar.projectKey=crud_usuarios \
                  -Dsonar.sources=. \
                  -Dsonar.host.url=$SONARQUBE_URL \
                  -Dsonar.login=$SONARQUBE_TOKEN
                '''
            }
        }
    }
}
