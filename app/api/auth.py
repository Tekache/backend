from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.database import users_collection
from app.core.security import verify_password, create_access_token, create_refresh_token
from app.utils.rate_limit import rate_limit

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    email = form_data.username  # ✅ email is defined HERE
    password = form_data.password

    # ✅ rate limit AFTER email exists
    rate_limit(email)

    user = users_collection.find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = create_access_token({"sub": email})
    refresh_token = create_refresh_token({"sub": email})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }
