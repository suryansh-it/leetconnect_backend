from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, leaderboard,profile
from .config import settings

# Create FastAPI app
app = FastAPI(title="LeetConnect API")

# CORS: allow our Chrome extension origin to call these APIs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount routers
app.include_router(auth.router)
app.include_router(leaderboard.router)
app.include_router(profile.router)

# app/main.py
@app.on_event("startup")
async def on_startup():
    from .db import ensure_indexes
    await ensure_indexes()
