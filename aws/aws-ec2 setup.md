# AWS EC2 Setup Guide

## Objective

Launch an Ubuntu EC2 instance to host the Dockerized Flask application deployed by the Jenkins CI/CD pipeline.

---

# Prerequisites

- AWS Account
- SSH Client
- Key Pair (.pem)
- Internet Connection

---

# Step 1: Login to AWS

1. Open AWS Console.
2. Navigate to EC2.
3. Click **Launch Instance**.

---

# Step 2: Configure Instance

| Setting | Value |
|----------|-------|
| Name | cicd-flask-server |
| AMI | Ubuntu Server 24.04 LTS |
| Instance Type | t2.micro (Free Tier) |
| Architecture | x86_64 |
| Key Pair | Create or Select Existing |

---

# Step 3: Network Settings

Allow:

- SSH (22)
- HTTP (80)
- HTTPS (443)
- Custom TCP (5000)

Attach the security group created for this project.

---

# Step 4: Storage

| Volume | Size |
|---------|------|
| Root Volume | 20 GB gp3 |

---

# Step 5: Launch Instance

Click **Launch Instance**.

---

# Step 6: Connect to EC2

```bash
chmod 400 aws-key.pem

ssh -i aws-key.pem ubuntu@YOUR_EC2_PUBLIC_IP
```

---

# Step 7: Update Ubuntu

```bash
sudo apt update
sudo apt upgrade -y
```

---

# Step 8: Install Git

```bash
sudo apt install git -y

git --version
```

---

# Step 9: Install Docker

```bash
curl -fsSL https://get.docker.com | sudo sh
```

---

# Step 10: Add User to Docker Group

```bash
sudo usermod -aG docker ubuntu

newgrp docker
```

Verify:

```bash
docker --version

docker ps
```

---

# Step 11: Install Docker Compose

```bash
sudo apt install docker-compose-plugin -y
```

Verify:

```bash
docker compose version
```

---

# Step 12: Test Docker

```bash
docker run hello-world
```

---

# Step 13: Verify Server

```bash
hostname

docker ps

docker images

free -h

df -h
```

---

# Ready for Jenkins Deployment

The EC2 instance is now ready to receive deployments from Jenkins.
