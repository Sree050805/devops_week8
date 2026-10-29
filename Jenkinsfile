
pipeline {
    agent any

    environment {
        PATH = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:${env.PATH}"
        KUBECONFIG = "/Users/sreejanadgoud/.kube/config"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Build Docker Image'
                sh 'docker build -t myfirstpythonapp:regevent .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_TOKEN'
                )]) {
                    sh '''
                        echo "$DOCKER_TOKEN" | docker login \
                          -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo 'Push Docker Image to Docker Hub'
                sh 'docker tag myfirstpythonapp:regevent sreeja6/devops_week9:regevent'
                sh 'docker push sreeja6/devops_week9:regevent'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploy Application to Kubernetes'
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
                sh 'kubectl rollout restart deployment/kubedemoapp-deployment'
                sh 'kubectl rollout status deployment/kubedemoapp-deployment --timeout=180s'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
