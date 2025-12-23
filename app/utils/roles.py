from fastapi import Depends, HTTPException
from app.utils.jwt_guard import get_current_user

def require_role(role: str):
    def checker(user=Depends(get_current_user)):
        if user.get("role") != role:
            raise HTTPException(status_code=403, detail="Access denied")
        return user
    return checker
