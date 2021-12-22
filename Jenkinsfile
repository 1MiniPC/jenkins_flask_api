pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            sh '''
            echo "building the repo"
            pip install -r requirements.txt
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
