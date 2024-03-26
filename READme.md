# Jenkins

Docker can be used within Jenkins to create isolated environments to run build and test tasks. This is done by setting up Docker as a Jenkins agent. Jenkins agents are programs that run on a machine and communicate back to the Jenkins master (the Jenkins server itself). This allows the Jenkins master to offload work and execute multiple tasks at once.

Jenkins is an open-so§urce automation server that enables developers to build, test, and deploy their software. It supports version control tools like Git, Subversion, and Mercurial, and can execute Apache Ant and Apache Maven-based projects, as well as arbitrary shell scripts and Windows batch commands.

To set up Docker in Jenkins, you need to install the Docker plugin on your Jenkins server. After that, you can define Docker as a Jenkins agent in your Jenkins system settings.

Once Docker is set up, you can use Jenkins pipelines that define the steps of your build process. In the pipeline script, you can define Docker commands to create and run Docker containers. Once the build task is completed, the Docker container is destroyed.

Please note that this is a high-level overview. For detailed instructions, please refer to Jenkins and Docker documentation.

Here are the commands for installing Jenkins on different platforms:

**Ubuntu:**

```bash
sudo apt update
sudo apt install openjdk-11-jdk
wget -q -O - <https://pkg.jenkins.io/debian/jenkins.io.key> | sudo apt-key add -
echo deb <http://pkg.jenkins.io/debian-stable> binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list
sudo apt update
sudo apt install jenkins

```

**Mac:**

```bash
brew install jenkins-lts
brew service start  jenkins-lts

```

**Windows:**
For Windows, you need to download the Jenkins installer. Here's the command to download it using PowerShell:

```bash
Invoke-WebRequest -Uri <https://get.jenkins.io/war-stable/latest/jenkins.war> -OutFile jenkins.war

```

Then you can run Jenkins with the command:

```bash
java -jar jenkins.war

```

**Docker:**

```bash
docker run \
-d \
-v /var/run/docker.sock:/var/run/docker.sock \
-v $(which docker):/usr/bin/docker \
-v jenkins_home:/var/jenkins_home \
--name jenkins \
-p 8080:8080 \
-p 50000:50000 \
jenkins/jenkins

```

## jenkins file with all fucntionallity


```
pipeline {
    agent any
    
    parameters {
        string(name: 'PARAMETER_NAME', defaultValue: 'default', description: 'Description of parameter')
        choice(name: 'CHOICE_PARAMETER', choices: ['Option1', 'Option2', 'Option3'], description: 'Description of choice parameter')
    }
    
    environment {
        ENV_VARIABLE = 'value'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            agent {
                docker {
                    image 'maven:latest'
                    args '-v $HOME/.m2:/root/.m2'
                }
            }
            steps {
                sh 'mvn clean package'
            }
        }
        
        stage('Test and Deploy') {
            parallel {
                stage('Test') {
                    steps {
                        sh 'mvn test'
                    }
                }
                stage('Deploy') {
                    when {
                        expression {
                            params.CHOICE_PARAMETER == 'Option1'
                        }
                    }
                    steps {
                        sh 'echo Deploying...'
                    }
                }
            }
        }
        
        stage('Deploy to Production') {
            when {
                branch 'master'
            }
            steps {
                sh 'echo Deploying to production...'
            }
        }
        
        stage('Notifications') {
            steps {
                slackSend(color: '#00FF00', message: "Build successful - ${env.JOB_NAME} ${env.BUILD_NUMBER}")
                emailext subject: "Build Notification", body: "Build ${env.JOB_NAME} ${env.BUILD_NUMBER} was successful.", to: "user@example.com"
            }
        }
    }
    
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if unstable'
        }
        changed {
            echo 'This will run only if the state changed'
        }
        aborted {
            echo 'This will run only if aborted'
        }
        cleanup {
            echo 'This will run at the end of pipeline'
        }
    }
}
```
