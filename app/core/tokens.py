from itsdangerous import URLSafeTimedSerializer
from app.config import settings

serializer = URLSafeTimedSerializer(settings.SECRET_KEY)


def generate_email_token(email: str):
    return serializer.dumps(email, salt="email-verify")


def verify_email_token(token: str, max_age=3600):
    return serializer.loads(token, salt="email-verify", max_age=max_age)
    
def generate_password_reset_token(email: str):
    return serializer.dumps(email, salt="password-reset")


def verify_password_reset_token(token: str, max_age=1800):
    return serializer.loads(token, salt="password-reset", max_age=max_age)

