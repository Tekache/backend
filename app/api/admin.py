from fastapi import APIRouter, Depends
from app.database import users_collection
from app.utils.roles import require_role

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/users", dependencies=[Depends(require_role("admin"))])
def list_users():
    return list(users_collection.find({}, {"password": 0}))

@router.post("/promote/{email}", dependencies=[Depends(require_role("admin"))])
def promote_user(email: str):
    users_collection.update_one(
        {"email": email},
        {"$set": {"role": "admin"}}
    )
    return {"status": "promoted"}

# from fastapi import APIRouter, Depends
# from app.database import users_collection

# router = APIRouter(prefix="/admin", tags=["Admin"])

# @router.get("/users")
# def get_all_users():
#     return list(users_collection.find({}, {"password": 0}))
