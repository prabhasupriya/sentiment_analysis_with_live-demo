# backend/services/alerting.py
def send_email(to_email: str, subject: str, body: str) -> bool:
    # actual email sending code
    print(f"Sending email to {to_email} with subject '{subject}'")
    return True  # mock behavior for testing

def send_alert(alert_type: str, message: str):
    # call send_email internally
    send_email("admin@example.com", f"Alert: {alert_type}", message)
