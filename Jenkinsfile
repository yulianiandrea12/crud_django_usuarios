pipeline {
    agent any

    tools {
        // El plugin de Python NO usa "python", así que lo quitamos
        // Tampoco existe "sonarQubeScanner" como herramienta
    }

    environment {
        // Este nombre debe coincidir con la configuración de Manage Jenkins → SonarQube Servers
        SONARQUBE_ENV = credentials('sonarqube-token')
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
                withSonarQubeEnv('sonarqube') {
                    sh '''
                    . venv/bin/activate
                    sonar-scanner \
                      -Dsonar.projectKey=crud_usuarios \
                      -Dsonar.sources=. \
                      -Dsonar.host.url=http://10.255.255.254:9000 \
                      -Dsonar.login=$SONARQUBE_ENV
                    '''
                }
            }
        }
    }
}
