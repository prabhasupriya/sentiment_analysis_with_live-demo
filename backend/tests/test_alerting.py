# backend/tests/test_alerting.py
from unittest.mock import patch
from backend.services.alerting import send_alert

def test_send_alert():
    # Patch send_email inside the alerting module
    with patch("backend.services.alerting.send_email", return_value=True) as mock_send:
        send_alert("Test Alert", "This is a test message")
        mock_send.assert_called_once_with("admin@example.com", "Alert: Test Alert", "This is a test message")
