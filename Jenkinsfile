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
                sh 'curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/html.tpl > html.tpl'
                sh 'mkdir -p reports'
                sh 'trivy image --ignore-unfixed --format template --template "@html.tpl" -o reports/api_calc-scan.html api_calc:latest'
                publishHTML target : [
                    allowMissing: true,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'api_calc-scan.html',
                    reportName: 'Trivy Scan',
                    reportTitles: 'Trivy Scan'
                ]

                // Scan again and fail on CRITICAL vulns
                sh 'trivy image --ignore-unfixed --exit-code 1 --severity CRITICAL api_calc:latest'
            }
        }
        stage('Scan with Semgrep') {
            steps {
                sh '''#!/bin/bash
                python3 -m venv .venv
                source .venv/bin/activate
                pip3 install semgrep
                semgrep api_calc.py
                deactivate'''
            }
        }
    }
}

