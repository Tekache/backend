from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "test_db"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

users_collection = db["users"]
audit_logs_collection = db["audit_logs"]
