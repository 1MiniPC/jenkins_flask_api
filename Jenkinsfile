pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            sh '''
            python3 -m pip install --upgrade pip
            which python3
            echo "building the repo"
            virtualenv venv
            . venv/bin/activate
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
