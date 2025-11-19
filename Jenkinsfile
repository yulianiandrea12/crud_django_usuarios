pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git url: 'https://github.com/yulianiandrea12/crud_django_usuarios.git', branch: 'main'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh """
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                """
            }
        }

        stage('Ejecutar pruebas Django') {
            steps {
                sh """
                    . venv/bin/activate
                    python manage.py test
                """
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo 'SonarQube no configurado todavía, se activará en el siguiente paso'
            }
        }

    }
}
