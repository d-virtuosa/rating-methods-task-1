pipeline {
    agent any

    stages {
        stage('Scan code with Semgrep') {
            steps {
                sh '''#!/bin/bash
                python3 -m venv .venv
                source .venv/bin/activate
                pip3 install semgrep
                semgrep --config=auto --junit-xml -o reports/api_calc-scan.xml api_calc.py
                deactivate'''
                junit skipMarkingBuildUnstable: true, testResults: 'reports/api_calc-scan.xml'
            }
        }
        stage('Removing previous image') {
            steps {
                sh 'docker stop $(docker container ls -q)'
            }
        }
        stage('Build container') {
            steps {
                sh 'docker build -f Dockerfile -t api_calc .'
            }
        }
        stage('Scan container with Trivy') {
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
        stage('Run container after scans') {
            steps {
                sh 'docker run -d -p 5000:5000 api_calc:latest'
            }
        }
    }
}

