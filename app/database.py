from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

client = AsyncIOMotorClient(settings.MONGODB_URI)
database = client[settings.DATABASE_NAME]

users_collection = database["users"]
audit_logs_collection = database["audit_logs"]
