from datetime import datetime
from bson import ObjectId
from app.database import database
from app.core.security import hash_password


async def create_user(user_data: dict):
    user_data["password"] = hash_password(user_data["password"])
    user_data["is_active"] = True
    user_data["created_at"] = datetime.utcnow()

    result = await database.users.insert_one(user_data)
    return str(result.inserted_id)


async def get_user_by_email(email: str):
    return await database.users.find_one({"email": email})
