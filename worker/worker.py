import asyncio
import redis

from worker.services.sentiment_analyzer import SentimentAnalyzer
from worker.processor import save_post_and_analysis

class SentimentWorker:
    def __init__(self, redis_client, stream, group):
        self.redis = redis_client
        self.stream = stream
        self.group = group
        self.analyzer = SentimentAnalyzer()

        try:
            self.redis.xgroup_create(stream, group, mkstream=True)
        except:
            pass

    async def process_message(self, msg_id, data):
        try:
            sentiment = await self.analyzer.analyze_sentiment(data["content"])
            emotion = await self.analyzer.analyze_emotion(data["content"])
            await save_post_and_analysis(data, sentiment, emotion)
            self.redis.xack(self.stream, self.group, msg_id)
        except Exception as e:
            print("Error:", e)

    async def run(self):
        while True:
            msgs = self.redis.xreadgroup(
                self.group,
                "worker-1",
                {self.stream: ">"},
                count=10,
                block=5000
            )

            for _, batch in msgs:
                await asyncio.gather(
                    *[self.process_message(mid, data) for mid, data in batch]
                )

if __name__ == "__main__":
    r = redis.Redis(host="redis", port=6379, decode_responses=True)
    worker = SentimentWorker(r, "sentiment-stream", "sentiment-group")
    asyncio.run(worker.run())
