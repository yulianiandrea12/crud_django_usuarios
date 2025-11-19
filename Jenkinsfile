pipeline {
    agent any

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
    }
}
