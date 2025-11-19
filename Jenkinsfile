pipeline {
    agent any

    tools {
        python 'Python3'
        sonarQubeScanner 'sonar-scanner'
    }

    environment {
        SONARQUBE_ENV = credentials('sonarqube-token')
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
                        -Dsonar.python.coverage.reportPaths=coverage.xml \
                        -Dsonar.host.url=http://10.255.255.254:9000 \
                        -Dsonar.login=$SONARQUBE_ENV
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
