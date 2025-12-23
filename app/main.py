from fastapi import FastAPI
from app.api import auth, users, audit, admin

app = FastAPI(title="Security Information System")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(audit.router)
app.include_router(admin.router)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"status": "Backend running cleanly"}
