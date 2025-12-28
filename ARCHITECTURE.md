# Sentiment Analysis Platform – System Architecture

## Overview
This system is a distributed, containerized sentiment analysis platform designed to ingest social media posts, analyze sentiment and emotions in real time, store results, and visualize insights on a live dashboard.

The architecture follows an event-driven microservices approach using Redis Streams for reliable message processing.


## System Components

### 1. Frontend (React + Vite)
- Displays sentiment distribution, trends, and real-time updates
- Connects to backend REST APIs and WebSocket
- Uses Recharts for data visualization

### 2. Backend API (FastAPI)
- Exposes REST endpoints:
  - `/api/health`
  - `/api/posts`
  - `/api/aggregate`
  - `/api/distribution`
- Provides WebSocket endpoint for real-time updates
- Handles alert detection logic
- Communicates with PostgreSQL and Redis

### 3. Ingester Service
- Simulates or ingests social media posts
- Publishes posts into Redis Streams
- Applies rate limiting and error handling

### 4. Worker Service
- Consumes messages from Redis Streams using consumer groups
- Performs sentiment and emotion analysis
- Stores results in PostgreSQL
- Acknowledges messages only after successful processing

### 5. PostgreSQL (Database)
- Stores:
  - Social media posts
  - Sentiment analysis results
  - Alerts
- Uses indexes for efficient querying
- Tables initialized automatically at startup using SQLAlchemy

### 6. Redis
- Redis Streams used for reliable message ingestion
- Redis caching used for frequently requested API responses



## Data Flow

Ingester
↓
Redis Streams
↓
Worker
↓
PostgreSQL
↓
Backend API
↓
Frontend Dashboard + WebSocket Clients

yaml
Copy code



## Technology Choices
- FastAPI for high-performance async APIs
- SQLAlchemy ORM for database abstraction
- Redis Streams for reliable, scalable messaging
- Hugging Face models for sentiment and emotion detection
- Docker Compose for local orchestration



## Scalability Considerations
- Multiple workers can be added to the same Redis consumer group
- Stateless backend allows horizontal scaling
- Redis Streams ensure no message loss
- Database indexes support high query throughput



## Security Considerations
- No hardcoded credentials
- Environment variables managed via `.env`
- Internal services not exposed to host
- WebSocket connections handled with cleanup on disconnect