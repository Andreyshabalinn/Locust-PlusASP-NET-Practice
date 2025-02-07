# Load Testing with Locust and ASP.NET

This project provides a simple ASP.NET web server and a Locust-based load testing environment. The setup ensures that only Locust can access the ASP.NET server, while the Locust UI remains available for external users to run tests.

## Features
- **ASP.NET Core Web API**: A minimal web server running on port `5000` inside a private network.
- **Locust Load Testing**: Locust is used to generate load and test the performance of the web server.
- **Isolated Networking**: The ASP.NET server is hidden from external access but available to Locust.
- **Docker Compose Setup**: Easily start and manage both services using Docker Compose.

## Prerequisites
Before you start, ensure you have:
- **Docker** installed ([Download Docker](https://www.docker.com/get-started))
- **Docker Compose** installed (included with Docker Desktop)

## Installation and Usage
### 1. Clone the Repository
```sh
git clone https://github.com/Andreyshabalinn/Locust-PlusASP-NET-Practice.git
cd LoadTestServer
```

### 2. Build and Start the Services
```sh
docker-compose up --build
```
This will:
- Build and start the ASP.NET server (`web` service)
- Build and start the Locust testing environment (`locust` service)

### 3. Access Locust UI
Once the services are running, open **Locust UI** in your browser:
```
http://localhost:8089
```
From here, you can configure and start load tests.

### 4. Running Load Tests
In the Locust UI:
1. Set **Host** to `http://web:5000` (Locust will resolve this internally)
2. Choose the number of users and spawn rate
3. Click **Start Swarming**

Alternatively, you can run Locust in headless mode via the command line:
```sh
docker-compose run locust locust -f locustfile.py --host=http://web:5000 --users 10 --spawn-rate 2 --run-time 1m
```

### 5. Stopping the Services
To stop all running containers, use:
```sh
docker-compose down
```

## Project Structure
```
project-root/
│
├── LocustTestServer/        # ASP.NET Web API
│   ├── Dockerfile          
│   ├── Program.cs
│   ├── ...
│
├── locust/                  # Locust load testing
│   ├── Dockerfile           
│   ├── locustfile.py       
│   ├── requirements.txt    
│
└── docker-compose.yml       # Docker Compose configuration
```

## Networking Overview
This project uses two networks:
1. **`backend-network`**: Used by ASP.NET and Locust for internal communication. The ASP.NET server is **not** accessible externally.
2. **`frontend-network`**: Used by Locust UI to allow external users to start load tests.

| Service  | Frontend Network | Backend Network | Access |
|----------|-----------------|-----------------|--------|
| **ASP.NET (web)**  | ❌ No  | ✅ Yes  | Only Locust |
| **Locust (locust)** | ✅ Yes  | ✅ Yes  | UI available |
| **Client (browser)** | ✅ Yes  | ❌ No  | Can access Locust UI |

## Notes
- If you want to test another server, update the `LOCUST_HOST` environment variable in `docker-compose.yml`.
- The Locust UI (`http://localhost:8089`) allows you to configure load tests dynamically.

---
🚀 Happy Load Testing!

