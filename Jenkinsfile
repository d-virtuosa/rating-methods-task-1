pipeline {
    agent any

    stages {
        
        stage('Build and run container') {
            steps {
                bash 'docker build -f Dockerfile -t api_calc .'
		bash 'docker run -d -p 5000:5000 api_calc:latest'
            }
        }
    }
}
