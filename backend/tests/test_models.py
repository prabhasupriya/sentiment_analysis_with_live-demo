# backend/tests/test_models.py
import pytest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models.database import Base
from backend.models.models import SocialMediaPost, SentimentAnalysis, SentimentAlert

@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = Session()
    yield session
    session.close()

def test_social_media_post(session):
    post = SocialMediaPost(post_id="123", source="Twitter", content="Hello world", author="Prabha", created_at=datetime.now())
    session.add(post)
    session.commit()
    assert session.query(SocialMediaPost).count() == 1

def test_sentiment_analysis(session):
    post = SocialMediaPost(post_id="123", source="Twitter", content="Hello world")
    session.add(post)
    session.commit()
    sentiment = SentimentAnalysis(post_id="123", model_name="BERT", sentiment_label="Positive", confidence_score=0.95, emotion="Happy")
    session.add(sentiment)
    session.commit()
    assert session.query(SentimentAnalysis).count() == 1

def test_sentiment_alert(session):
    alert = SentimentAlert(alert_type="Negative Spike", threshold_value=0.7, actual_value=0.8,
                           window_start=datetime.now(), window_end=datetime.now(),
                           post_count=5, details={"sample": 1})
    session.add(alert)
    session.commit()
    assert session.query(SentimentAlert).count() == 1
