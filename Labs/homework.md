# Jenkins assignments

setup:

- If you have created the **Jenkinsfile** on Github , it time to update the Devops Pipeline
- So go to Jenkins and update the Pipeline Definition section , change the Pipeline Script option to Pipeline Script from SCM
- Then select SCM as Git
- Add the Repo Clone HTTPS URL in **Repository URL** section
- For Credentials , Create Username and Password type of credentials with your GitHub email/password
- Update the Branch to Main

# **Task 1 - Jenkins Free Style Job Setup**

Setup the Jenkins Free Style Job to meet the below requirements:

- Create a new Free Style Jenkins Job and name it as **Docker-Verify**.
- Run Shell Command from inside the Jenkins Job to Verify the Docker Version on the Jenkins machine.

Hint:

```jsx
 **docker --version** 
```

# **Task 2 - Jenkins Free Style Job , Cron Setup**

Setup the Jenkins Free Style Job to meet the below requirements:

- Update your Free Style Jenkins Job **Docker-Verify**
- Set the job to run every minute on Jenkins

# **Task 3 - Jenkins Free Style Job , Parameters**

Setup the Jenkins Free Style Job to meet the below requirements:

- Update your Free Style Jenkins Job **Docker-Verify**
- Remove the cron from the job to avoid running it every minute.
- Configure your job as parameterized job , add choice section in your job.
- Under the choices section add two options , **docker** and **python.**
- Then update your execute shell command to get the version of package selected by the user.

# **Task 4 - Jenkins Declarative Pipeline , Docker Verify Stage Setup**

Setup the Jenkins Declarative Pipeline to meet the below requirements:

- Create a new Jenkins job of type **Pipeline**
- Name your Job as **Devops**
- Add single stage named as 'Docker-Verify'
- Setup the command under steps section **'docker --version'**
- Build the Pipeline to print the Docker Version in the output

# **Task 5 - Jenkins Declarative Pipeline -> Git Verify Stage Setup**

- Update your Jenkins Pipeline **Devops.**
- Add a new stage named as 'Git-Verify'
- Setup the command under steps section **'git --version'**
- Build the Pipeline to print the Docker Version and Git Version in the output

# **Task 6 Jenkins Declarative Pipeline -,Docker build**

Setup the GitHub Repo to meet the below requirements:

- Go to GutHub Repo
- Upload the attached Dockerfile onto your GitHub Repo
- Dockerfile:

```docker
From httpd
LABEL name="devops"
```

Setup/Update the Jenkins Declarative Pipeline to meet the below requirements:

- Update your JenkinsFile to add one more stage named as **'Docker-Build'**
- Inside the Steps section of stage **'Docker-Build'** add a **to build the image with environments as names and tag for the image**
- Then Run the DevOps Pipeline after Jenkinsfile is updated

# **Task 7 - Jenkins Declarative Pipeline , Docker Image Verify Stage**

- Update your JenkinsFile to add one more stage named as **'Docker-Image-Verify'**
- Inside the Steps section of stage **'Docker-Image-Verify'** add a command  **to show all the images filtered by the tagname env (the same name we had for the build)**
- Then Run the DevOps Pipeline after Jenkinsfile is updated

# **Task 8 - Jenkins Declarative Pipeline -> Jenkins Pre Defined Variables**

- Inside the Steps section of stage **'Docker-Build'** update the docker build command to use the Jenkins Build Number as tag value, So basically the tag value of our docker image will be always updated.
- Then Run the DevOps Pipeline after Jenkinsfile is updated

Hint: