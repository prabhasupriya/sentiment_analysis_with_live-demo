from backend.services.sentiment_analyzer import RuleBasedSentimentAnalyzer

def test_end_to_end_flow():
    analyzer = RuleBasedSentimentAnalyzer()
    result = analyzer.analyze("I love this platform")
    assert result["sentiment"] == "positive"
