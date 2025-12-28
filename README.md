# Real-Time Sentiment Analysis Platform

This project is a full-stack, real-time sentiment analysis platform that ingests text data, analyzes sentiment and emotions, stores results, and visualizes insights on a live dashboard.  
The system supports real-time updates using WebSockets and REST APIs.



## Features

- Real-time sentiment analysis (positive / negative / neutral)
- Emotion detection
- Live dashboard with charts
- REST APIs for analytics
- WebSocket-based real-time updates
- Redis Streams for reliable ingestion
- Fully Dockerized microservice architecture



## System Architecture

The platform consists of six services:

1. Frontend (React)
2. Backend API (FastAPI)
3. Ingester service
4. Worker service
5. PostgreSQL database
6. Redis (Streams + Cache)

 See detailed architecture in **ARCHITECTURE.md**



## Prerequisites

- Docker 20.10+
- Docker Compose v2+
- Minimum 4 GB RAM
- Open ports:
  - 3000 (Frontend)
  - 8000 (Backend)



## Setup Instructions

```bash
# Clone repository
git clone https://github.com/prabhasupriya/sentiment-platform.git
cd sentiment-platform

# Create environment file
cp .env.example .env

# Start all services
docker-compose up -d

# Verify services
docker-compose ps
Access the Application
Frontend Dashboard: http://localhost:3000

Backend Health Check: http://localhost:8000/api/health

Expected response:

json
Copy code
{"status": "ok"}
API Endpoints
Method	Endpoint	Description
GET	/api/health	Health check
GET	/api/posts	Paginated posts
GET	/api/aggregate	Sentiment trends
GET	/api/distribution	Sentiment distribution
WS	/ws	Real-time updates

Testing
bash
Copy code
docker-compose exec backend pytest -v
docker-compose exec backend pytest --cov=backend --cov-report=term
Minimum required coverage: 70%
Current coverage: ~98%

Stopping the System
bash
Copy code
docker-compose down
Security Notes
No hardcoded credentials

Secrets managed via environment variables

Internal services not exposed to host

Redis and PostgreSQL are private to the Docker network