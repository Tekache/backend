from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "CHANGE_ME_SECRET"
ALGORITHM = "HS256"

def create_token(data: dict, minutes: int):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
