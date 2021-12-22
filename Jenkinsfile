pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            sh '''
            python3 --version
            echo "building the repo"
            apt-get update
            apt-get -y install python3-pip
            pip3 install -r requirements.txt
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
