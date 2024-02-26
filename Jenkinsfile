pipeline {
    agent any
    environment {
        DOCKER_IMAGE_TAG = 'idubi/flask-htm:latest'
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('-t ${DOCKER_IMAGE_TAG} ./exFlaskWeb/')
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                     withCredentials([usernamePassword(credentialsId: 'idubi_docker', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) 
                                    {
                        docker.withRegistry('hhttps://hub.docker.com/repository/docker/idubi', 'idubi_docker') 
                                            {
                                                   docker.image('${DOCKER_IMAGE_TAG}').push()
                                            }
                                    }
                    }
                }
            }
        }
    }
}

   withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                            docker.image(DOCKER_IMAGE_TAG).push()
                            