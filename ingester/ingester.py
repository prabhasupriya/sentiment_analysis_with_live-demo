import asyncio, random, time, logging
from datetime import datetime
import redis

logging.basicConfig(level=logging.INFO)

class DataIngester:
    def __init__(self, redis_client, stream_name, posts_per_minute=60):
        self.redis = redis_client
        self.stream = stream_name
        self.delay = 60 / posts_per_minute

        self.positive = [
            "I absolutely love {product}!",
            "{product} is amazing!",
            "Great experience with {product}"
        ]
        self.negative = [
            "I hate {product}",
            "Terrible experience with {product}",
            "Very disappointed with {product}"
        ]
        self.neutral = [
            "Just tried {product}",
            "Using {product} today",
            "Received {product}"
        ]
        self.products = ["ChatGPT", "iPhone 16", "Netflix", "Tesla Model 3"]

    def generate_post(self):
        sentiment_choice = random.choices(
            ["pos", "neg", "neu"], weights=[40,30,30]
        )[0]

        template = random.choice(
            self.positive if sentiment_choice=="pos"
            else self.negative if sentiment_choice=="neg"
            else self.neutral
        )

        content = template.format(product=random.choice(self.products))
        return {
            "post_id": f"post_{int(time.time()*1000)}",
            "source": random.choice(["twitter", "reddit"]),
            "content": content,
            "author": f"user_{random.randint(1000,9999)}",
            "created_at": datetime.utcnow().isoformat() + "Z"
        }

    async def publish_post(self, post):
        try:
            self.redis.xadd(self.stream, post)
            logging.info(f"Published {post['post_id']}")
            return True
        except Exception as e:
            logging.error(e)
            return False

    async def start(self):
        while True:
            post = self.generate_post()
            await self.publish_post(post)
            await asyncio.sleep(self.delay)

if __name__ == "__main__":
    r = redis.Redis(host="redis", port=6379, decode_responses=True)
    ingester = DataIngester(r, "social_stream")
    asyncio.run(ingester.start())
