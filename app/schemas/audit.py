from pydantic import BaseModel
from datetime import datetime


class AuditLogResponse(BaseModel):
    user_email: str
    action: str
    timestamp: datetime
