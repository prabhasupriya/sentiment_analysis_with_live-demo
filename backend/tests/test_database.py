# backend/tests/test_database.py
import pytest

def test_engine_exists():
    # import inside function to avoid circular import
    from backend.models.database import engine
    assert engine is not None

def test_session_local():
    from backend.models.database import SessionLocal
    from sqlalchemy.orm import Session
    session = SessionLocal()
    assert isinstance(session, Session)
    session.close()

def test_base_metadata():
    from backend.models.database import Base
    assert hasattr(Base, "metadata")
