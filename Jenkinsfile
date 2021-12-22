pipeline {
  agent any
  stages {
    stage('Check run') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'githubapp-jenkins',
                                          usernameVariable: '1minipc',
                                          passwordVariable: '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')]) {
            sh '''
            curl -H "Content-Type: application/json" \
                 -H "Accept: application/vnd.github.antiope-preview+json" \
                 -H "authorization: Bearer ${GITHUB_ACCESS_TOKEN}" \
                 -d '{ "name": "check_run", \
                       "head_sha": "'${GIT_COMMIT}'", \
                       "status": "in_progress", \
                       "external_id": "42", \
                       "started_at": "2020-03-05T11:14:52Z", \
                       "output": { "title": "Check run from Jenkins!", \
                                   "summary": "This is a check run which has been generated from Jenkins as GitHub App", \
                                   "text": "...and that is awesome"}}' https://api.github.com/repos/<org>/<repo>/check-runs
            '''
        }
      }
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            '''
            sh 'echo "building the repo"'
            sh 'pip install -r requirements.txt'
            '''
          }
        }
      }
    }

    stage('Test') {
      steps {
        sh 'python3 app.py'
      }
    }

    stage('Deploy')
    {
      steps {
        echo "deploying the application"
      }
    }

  }

}
