# End-to-End-CI-CD-Pipeline-using-Jenkins-and-AWS-docker

This project demonstrates the implementation of a complete Continuous Integration and Continuous Deployment (CI/CD) pipeline for a Dockerized Python Flask application. The pipeline automates the software delivery lifecycle, from source code management to deployment on an Amazon EC2 instance.

## Key Features

- Automated CI/CD pipeline using Jenkins
- GitHub Webhook integration
- Dockerized Python Flask application
- SonarQube static code analysis

## Project Architecture

![image alt](https://github.com/Abhi-anand735/End-to-End-CI-CD-Pipeline-using-Jenkins-and-AWS-docker/blob/452e7f01bf0855fc3c4b5134b6d534473028c5dd/images/ChatGPT%20Image%20Jul%205%2C%202026%2C%2005_51_23%20PM.png)

## Technology Stack

The following technologies and tools are used to implement the CI/CD pipeline and deploy the application.

| Category               | Technology                  |
| ---------------------- | --------------------------- |
| Programming Language   | Python 3.12                 |
| Backend Framework      | Flask                       |
| Version Control        | Git                         |
| Source Code Repository | GitHub                      |
| Continuous Integration | Jenkins                     |
| Code Quality           | SonarQube Community Edition |
| Containerization       | Docker                      |
| Container Registry     | Docker Hub                  |
| Cloud Platform         | Amazon Web Services (AWS)   |
| Compute Service        | AWS EC2                     |
| Reverse Proxy          | Nginx                       |
| Operating System       | Ubuntu Server 24.04 LTS     |
| Automation             | Shell Script                |
| Package Manager        | pip                         |          
| Documentation          | Markdown                    |
| IDE                    | Visual Studio Code          |

---

## Prerequisites

Before running this project, ensure that the following software and services are installed and configured.

| Software                    | Recommended Version   |
| --------------------------- | --------------------- |
| Python                      | 3.12 or later         |
| Git                         | Latest Stable Version |
| Docker                      | Latest Stable Version |
| Docker Compose              | v2.x                  |
| Jenkins                     | LTS Release           |
| SonarQube Community Edition | Latest LTS            |
| Java                        | JDK 17 or later       |
| Visual Studio Code          | Latest Version        |
| AWS CLI (Optional)          | Version 2             |

---
 ## Setup
 
 - Step 1: Install Python Dependencies
   ````bash
   pip install -r requirements.txt
   ````

 - Step 2: Run the Application Locall
   ````bash
   http://localhost:5000
   ````

 - Step 3: Build the Docker Image
   ````bash
   docker build -t cicd-flask-app.
   ````

 - Step 4: Run the Docker Container
   ````bash
   docker run -d -p 5000:5000 cicd-flask-app
   ````

 - Step 5: Run Using Docker Compose
    ````bash
    docker compose up --build -d
    ````

 - Step 6: Execute the Jenkins Pipeline
    ````bash
    git add .
    git commit -m "Initial CI/CD Pipeline"
    git push origin main
    ````  
