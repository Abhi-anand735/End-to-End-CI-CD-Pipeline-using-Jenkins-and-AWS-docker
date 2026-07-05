# AWS Security Group Configuration

## Objective

Create a security group that allows Jenkins to deploy the application and users to access it.

---

# Create Security Group

Name:

```
cicd-security-group
```

Description:

```
Security Group for Jenkins CI/CD Project
```

---

# Inbound Rules

| Type | Protocol | Port | Source | Purpose |
|------|----------|------|--------|----------|
| SSH | TCP | 22 | My IP | Remote Login |
| HTTP | TCP | 80 | 0.0.0.0/0 | Web Traffic |
| HTTPS | TCP | 443 | 0.0.0.0/0 | Secure Web Traffic |
| Custom TCP | TCP | 5000 | 0.0.0.0/0 | Flask Application (Testing) |

---

# Outbound Rules

Allow All Traffic

| Type | Destination |
|------|-------------|
| All Traffic | 0.0.0.0/0 |

---

# Verify Ports

From your local machine:

```bash
curl http://YOUR_EC2_PUBLIC_IP:5000/health
```

Expected response:

```json
{
    "status":"UP"
}
```

---

# Production Recommendation

For production deployments:

- Expose only port 80 or 443.
- Use Nginx as a reverse proxy.
- Keep port 5000 accessible only internally.

---



