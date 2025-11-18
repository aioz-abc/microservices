from fastapi import FastAPI
from .controller import router as auth_router

app = FastAPI(title="Auth Service", version="0.1.0")

app.include_router(auth_router)
