from fastapi import APIRouter, Depends
from app.core.dependencies import require_role
from app.models.user import user_helper

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/admin")
async def admin_only(user=Depends(require_role("admin"))):
    return {"message": "Admin access granted"}
