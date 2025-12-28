# backend/models/models.py
from sqlalchemy import Column, String, Integer, Float, DateTime, JSON
from backend.models.database import Base
from datetime import datetime,timezone
from datetime import datetime, timezone
class SocialMediaPost(Base):
    __tablename__ = "social_media_posts"
    post_id = Column(String, primary_key=True, index=True)
    source = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author = Column(String, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class SentimentAnalysis(Base):
    __tablename__ = "sentiment_analysis"
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(String)
    model_name = Column(String)
    sentiment_label = Column(String)
    confidence_score = Column(Float)
    emotion = Column(String)

class SentimentAlert(Base):
    __tablename__ = "sentiment_alerts"
    id = Column(Integer, primary_key=True, index=True)
    alert_type = Column(String)
    threshold_value = Column(Float)
    actual_value = Column(Float)
    window_start = Column(DateTime)
    window_end = Column(DateTime)
    post_count = Column(Integer)
    details = Column(JSON)
