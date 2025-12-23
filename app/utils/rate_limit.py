from time import time
from fastapi import HTTPException

_attempts = {}

def rate_limit(key: str, limit=5, window=60):
    now = time()
    history = _attempts.get(key, [])
    history = [t for t in history if now - t < window]

    if len(history) >= limit:
        raise HTTPException(status_code=429, detail="Too many attempts")

    history.append(now)
    _attempts[key] = history

_attempts = {}

import time
def rate_limit(key: str, limit: int = 5, window: int = 60):
    now = time.time()
    attempts = _attempts.get(key, [])

    attempts = [t for t in attempts if now - t < window]

    if len(attempts) >= limit:
        raise Exception("Too many login attempts. Try later.")

    attempts.append(now)
    _attempts[key] = attempts
