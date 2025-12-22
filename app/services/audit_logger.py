from app.database import audit_logs_collection
from app.models.audit_log import AuditLog


async def log_event(
    event: str,
    action: str,
    user_id: str | None = None,
    ip_address: str | None = None,
):
    audit_log = AuditLog(
        event=event,
        action=action,
        user_id=user_id,
        ip_address=ip_address,
    )

    await audit_logs_collection.insert_one(audit_log.dict())
