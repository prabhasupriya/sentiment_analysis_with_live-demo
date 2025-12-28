class RuleBasedSentimentAnalyzer:
    POSITIVE = {
        "good", "great", "excellent", "happy", "love",
        "amazing", "awesome", "fantastic", "satisfied"
    }

    NEGATIVE = {
        "bad", "worst", "terrible", "hate", "sad",
        "angry", "poor", "awful", "disappointed"
    }

    EMOTIONS = {
        "joy": {"happy", "love", "excited"},
        "anger": {"angry", "furious", "hate"},
        "sadness": {"sad", "depressed"},
        "fear": {"scared", "afraid"},
        "surprise": {"wow", "amazed"}
    }

    def analyze(self, text: str) -> dict:
        if not isinstance(text, str) or not text.strip():
            return {"sentiment": "neutral", "confidence": 0.0}

        words = set(text.lower().split())
        pos = len(words & self.POSITIVE)
        neg = len(words & self.NEGATIVE)

        if pos > neg:
            sentiment = "positive"
        elif neg > pos:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        confidence = round(abs(pos - neg) / max(len(words), 1), 2)

        return {
            "sentiment": sentiment,
            "confidence": confidence
        }

    def detect_emotion(self, text: str) -> str:
        words = set(text.lower().split())
        for emotion, vocab in self.EMOTIONS.items():
            if words & vocab:
                return emotion
        return "neutral"

    def analyze_batch(self, texts: list[str]) -> list[dict]:
        return [self.analyze(text) for text in texts]
