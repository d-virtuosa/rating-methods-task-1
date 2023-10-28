pipeline {
    agent any
        //environment {
      // The following variable is required for a Semgrep Cloud Platform-connected scan:
            //SEMGREP_APP_TOKEN = credentials('cc8015c796d95df7d8aeee7964ec9c3fe115521c52fda88269830e28360678cf')

      // Uncomment the following line to scan changed
      // files in PRs or MRs (diff-aware scanning):
      // SEMGREP_BASELINE_REF = "main"

      // Troubleshooting:

      // Uncomment the following lines if Semgrep Cloud Platform > Findings Page does not create links
      // to the code that generated a finding or if you are not receiving PR or MR comments.
      // SEMGREP_JOB_URL = "${BUILD_URL}"
      // SEMGREP_COMMIT = "${GIT_COMMIT}"
      // SEMGREP_BRANCH = "${GIT_BRANCH}"
      // SEMGREP_REPO_NAME = env.GIT_URL.replaceFirst(/^https:\/\/github.com\/(.*).git$/, '$1')
      // SEMGREP_REPO_URL = env.GIT_URL.replaceFirst(/^(.*).git$/,'$1')
      // SEMGREP_PR_ID = "${env.CHANGE_ID}"
    //}
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
                sh 'trivy image --ignore-unfixed --vuln-type os,library --format template --template "@html.tpl" -o reports/api_calc-scan.html api_calc:latest'
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
                sh 'trivy image --ignore-unfixed --vuln-type os,library --exit-code 1 --severity CRITICAL api_calc:latest'
            }
        }
        stage('Scan with Semgrep') {
            steps {
                sh 'python3 -m venv .venv && source .venv/bin/activate && pip3 install semgrep && semgrep api_calc.py && deactivate'
            }
        }
    }
}

