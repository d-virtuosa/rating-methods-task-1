pipeline {
    agent any

    stages {
        stage('Removing previous image') {
            steps {
                bash 'running=$(docker ps -a | grep Up | cut -c1-12)'
		bash 'docker stop $running'
            }
        }
        stage('Build and run container') {
            steps {
                sh 'docker build -f Dockerfile -t api_calc .'
		sh 'docker run -d -p 5000:5000 api_calc:latest'
            }
        }
    }
}
