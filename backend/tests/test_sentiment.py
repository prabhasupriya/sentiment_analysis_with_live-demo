from backend.services.sentiment_analyzer import RuleBasedSentimentAnalyzer

analyzer = RuleBasedSentimentAnalyzer()


def test_sentiment_accuracy():
    cases = [
        ("I love this product", "positive"),
        ("This is the worst experience", "negative"),
        ("It is a device", "neutral"),
        ("I am very happy", "positive"),
        ("I hate this", "negative"),
    ]

    correct = 0
    for text, expected in cases:
        result = analyzer.analyze(text)["sentiment"]
        if result == expected:
            correct += 1

    accuracy = correct / len(cases)
    assert accuracy >= 0.8


def test_emotion_detection():
    assert analyzer.detect_emotion("I am very happy") == "joy"
    assert analyzer.detect_emotion("I am angry") == "anger"


def test_batch_processing():
    texts = ["I love it", "This is bad", "Okay"]
    results = analyzer.analyze_batch(texts)
    assert len(results) == 3
