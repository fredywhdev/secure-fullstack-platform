from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.users.router import router as users_router

app = FastAPI(title="Secure FullStack Platform")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(auth_router)
app.include_router(users_router)
