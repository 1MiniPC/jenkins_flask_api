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
            sh '''
            python --version
            pip install -r requirements.txt
            '''
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
