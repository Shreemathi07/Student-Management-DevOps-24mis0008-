pipeline {
    agent any
    stages {
        stage ('Source SCM Checkout') {
            steps {
                git branch: 'main', url: ''
            }
        }
        stage ('Execute Analytics Engine') {
            steps {
                dir('project1') {
                    bat 'python student_report.py'
                }
            }
        }
        stage ('Archive Output Logs') {
            steps {
                dir('project1') {
                    archiveArtifacts artifacts: 'academic_summary.txt', fingerprint: true
                }
            }
        }
    }
}
