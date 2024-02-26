pipeline {
    agent any
    environment {
        DOCKER_IMAGE_TAG = 'idubi/flask-htm:latest'
    }
    stages {
        stage('Print Current Working Directory') {
            steps {
                sh 'echo `ls -ltr ./exFlaskWeb/`'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('-t idubi/flask-htm:latest ./exFlaskWeb/ ')
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                     withCredentials([usernamePassword(credentialsId: 'idubi_docker', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) 
                                    {
                        docker.withRegistry('https://hub.docker.com/repositories/idubi', 'idubi_docker') 
                                            {
                                                   docker.image('idubi/flask-htm:latest').push()
                                            }
                                    }
                    }
                }
            }
        }
    }

 