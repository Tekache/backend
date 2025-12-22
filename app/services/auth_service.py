from app.services.user_service import get_user_by_email
from app.core.security import verify_password
from app.core.jwt import create_access_token


async def authenticate_user(email: str, password: str):
    user = await get_user_by_email(email)
    if not user:
        return None

    if not verify_password(password, user["password"]):
        return None

    token = create_access_token(
        data={
            "sub": str(user["_id"]),
            "role": user["role"]
        }
    )

    return token
