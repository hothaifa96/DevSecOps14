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

## initAdminPassword

To retrieve the initial admin password for a Jenkins Docker container, you can use the following command:
```bash
docker exec <container_name> cat /var/jenkins_home/secrets/initialAdminPassword
```