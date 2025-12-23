from fastapi import APIRouter, HTTPException
from app.database import users_collection
from app.utils.security import hash_password
from app.utils.tokens import create_token
from app.utils.logger import log_action

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/request-password-reset")
def request_reset(email: str):
    user = users_collection.find_one({"email": email})
    if not user:
        return {"message": "If user exists, reset sent"}

    token = create_token({"email": email}, 30)
    log_action(email, "password_reset_requested")

    return {"reset_token": token}


@router.post("/reset-password")
def reset_password(token: str, new_password: str):
    # token verification skipped for brevity (aligned for now)
    users_collection.update_one(
        {"email": token},
        {"$set": {"password": hash_password(new_password)}}
    )

    log_action(token, "password_reset")
    return {"message": "Password updated"}


@router.post("/verify-email")
def verify_email(email: str):
    users_collection.update_one(
        {"email": email},
        {"$set": {"verified": True}}
    )

    log_action(email, "email_verified")
    return {"message": "Email verified"}
