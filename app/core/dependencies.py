from fastapi import Depends, HTTPException, status
from app.core.security import get_current_user

def require_role(role: str):
    async def checker(user=Depends(get_current_user)):
        if user["role"] != role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )
        return user
    return checker
