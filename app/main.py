from fastapi import FastAPI
from app.api import auth, users

app = FastAPI(title="Security Information System")

app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return {"status": "Backend running cleanly"}
