from datetime import datetime
from app.database import audit_logs_collection

def log_action(user_id: str, action: str, meta: dict | None = None):
    audit_logs_collection.insert_one({
        "user_id": user_id,
        "action": action,
        "meta": meta or {},
        "timestamp": datetime.utcnow()
    })
