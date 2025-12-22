from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class AuditLog(BaseModel):
    event: str = Field(..., example="USER_LOGIN")
    user_id: Optional[str] = None
    action: str
    ip_address: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
