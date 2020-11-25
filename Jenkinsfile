pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
	sh 'pip install -e .'
      }
    }
    stage('test') {
      steps {
        echo 'To be implemented'
      }   
    }
  }
}
