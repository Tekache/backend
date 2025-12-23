from fastapi import APIRouter, Depends
from app.database import audit_logs_collection
from app.utils.roles import require_role

router = APIRouter(prefix="/audit", tags=["Audit"])

@router.get("/", dependencies=[Depends(require_role("admin"))])
def get_logs(limit: int = 20, skip: int = 0):
    logs = audit_logs_collection.find().skip(skip).limit(limit)
    return list(logs)
