
# Microservices Deployment with Docker Compose & Docker Swarm

This project demonstrates how to deploy a microservice-based application using **Docker Compose** for local development and **Docker Swarm** for production-like environments.

## 🏗️ Project Structure
```
my-microservices-app/
├── auth-service/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
├── user-service/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
├── docker-compose.yml
├── docker-stack.yml
└── .env
```

---

## 🚀 Step 1: Build and Run Using Docker Compose

### 1. **Build the Services**
```bash
docker-compose build
```
<p align="center">
  <img src="https://github.com/Himanshu5619/Docker-Container/blob/main/Exp7(Docker%20Compose%20%26%20Docker%20Swarm)/SS/Screenshot%202025-03-28%20094901.png" alt="Build the Services">
</p>
### 2. **Start the Services**
```bash
docker-compose up -d
```

### 3. **Check Running Containers**
```bash
docker-compose ps
```
<p align="center">
  <img src="https://github.com/Himanshu5619/Docker-Container/blob/main/Exp7(Docker%20Compose%20%26%20Docker%20Swarm)/SS/Screenshot%202025-03-28%20095556.png" alt="Build the Services">
</p>
### 4. **Test the Services**
```bash
curl http://localhost:5000/auth
curl http://localhost:5001/user
```

### 5. **Check Logs**
```bash
docker-compose logs -f auth-service
```

### 6. **Stop the Services**
```bash
docker-compose down
```

---

## 🌍 Step 2: Deploy Using Docker Swarm

### 1. **Initialize Swarm (on Manager Node)**
```bash
docker swarm init
```

### 2. **Add Worker Nodes**
On each worker node, run:
```bash
docker swarm join --token <TOKEN> <MANAGER_IP>:2377
```

### 3. **Verify Nodes**
```bash
docker node ls
```

### 4. **Build Docker Images**
```bash
docker build -t auth-service ./auth-service
docker build -t user-service ./user-service
```

### 5. **Deploy the Stack**
```bash
docker stack deploy -c docker-stack.yml myapp
```

### 6. **Check Running Services**
```bash
docker stack services myapp
```

### 7. **Check Service Tasks (Replicas)**
```bash
docker service ps myapp_auth-service
```

### 8. **View Logs**
```bash
docker service logs -f myapp_auth-service
```

### 9. **Scale a Service**
```bash
docker service scale myapp_auth-service=4
```

### 10. **Test Service Endpoints**
```bash
curl http://<MANAGER_NODE_IP>:5000/auth
curl http://<MANAGER_NODE_IP>:5001/user
```

### 11. **Remove Swarm Stack**
```bash
docker stack rm myapp
```

### 12. **Leave Swarm (on Worker Node)**
```bash
docker swarm leave
```

### 13. **Force Leave Swarm (on Manager Node)**
```bash
docker swarm leave --force
```

---

## 🔎 Troubleshooting

✅ **Check Container Logs:**
```bash
docker-compose logs <service_name>
```

✅ **Check Failed Services in Swarm:**
```bash
docker service ps <service_name>
```

✅ **Verify Port Bindings:**
```bash
docker ps
```

✅ **Check Docker Engine Status:**
```bash
systemctl status docker
```

✅ **Network Check:**
```bash
docker network inspect <network_name>
```

---

## 📋 Notes
- Use `.env` files for sensitive data and environment variables.
- Implement **health checks** for improved stability.
- Enable **logging** and **monitoring** for enhanced visibility.
- For secure production deployment, consider **Docker Secrets** for managing credentials.

---

### 🚨 Need Help?
Feel free to raise an issue or contribute to the project! 😊

