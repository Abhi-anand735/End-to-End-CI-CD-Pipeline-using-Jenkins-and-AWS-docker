- GitHub Webhook Not Triggering Jenkins
  * Cause:
    Incorrect webhook URL
  * debug:
    verify the webhook url

- Docker Build Failed
  * Cause:
    Missing Dockerfile, Invalid Dockerfile syntax
  * Debug:
    ````bash
    docker build -t cicd-flask-app
    ````

- Docker Login Failed
  * Cause:
    unauthorized: incorrect username or password
  * Debug:
    Verify Docker Hub username

- Docker Push Failed
  * Cause:
    denied: requested access to the resource is denied
  * Debug:
    Verify repository name,Ensure the repository exists on Docker Hub.

 - SSH Connection Failed
   * Cause:
     Port 22 is not open
   * Debug:
     Verify the SSH private key,Confirm the correct EC2 username (ubuntu for Ubuntu AMIs)

- Jenkins Pipeline Failed
  * Cause:
    Agent status is offline, credentials and permissions are correct.
  * Debug:
    Check the agent status, check the credentials and permissions. 
