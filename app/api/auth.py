from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreate
from app.database import users_collection
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
async def register(user: UserCreate):
    existing = await users_collection.find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = {
        "email": user.email,
        "hashed_password": hash_password(user.password),
        "role": "user",
    }
    await users_collection.insert_one(new_user)
    return {"message": "User registered"}

@router.post("/login")
async def login(user: UserCreate):
    db_user = await users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(
        user.password, db_user["hashed_password"]
    ):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(
        {"sub": db_user["email"], "role": db_user["role"]}
    )
    return {"access_token": token, "token_type": "bearer"}
