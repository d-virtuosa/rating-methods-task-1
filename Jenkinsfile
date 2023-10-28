pipeline {
    agent any

    stages {
        stage('Removing previous image') {
            steps {
                sh 'docker stop $(docker container ls -q)'
            }
        }
        stage('Build and run container') {
            steps {
                sh 'docker build -f Dockerfile -t api_calc .'
		sh 'docker run -d -p 5000:5000 api_calc:latest'
            }
        }
        stage('Scan with Trivy') {
            steps {
                sh 'trivy image --vuln-type os --ignore-unfixed -f json -o api_calc.json api_calc:latest'
            }
        }
    }
}
