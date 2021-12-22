pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            sh '''
            curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
            cp get-pip.py ~/usr/bin/python3/
            python3 ~/usr/bin/python3/get-pip.py
            pip3 --version
            echo "building the repo"
            virtualenv -p ~/usr/bin/python3 venv
            . venv/bin/activate
            pip3 install -r requirements.txt
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
