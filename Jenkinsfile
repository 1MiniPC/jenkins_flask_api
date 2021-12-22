pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          agent {
              docker {
                  image 'python:3-alpine'
              }
          }
          steps {
          withEnv(["HOME=${env.WORKSPACE}"]) {
              sh 'pip install --user -r requirements.txt'
          }
          }
        }
      }
    }

    stage('Test') {
      steps {
        sh 'python app.py &'
      }
    }

    stage('Deploy')
    {
      steps {
        sh '''
        echo "deploying the application"
        curl localhost:5000
        '''
      }
    }

  }

}
