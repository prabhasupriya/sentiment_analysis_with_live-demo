import redis.asyncio as redis

# Redis client
redis_client = redis.Redis(
    host="sentiment-redis",
    port=6379,
    decode_responses=True
)
