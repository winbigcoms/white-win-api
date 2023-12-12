from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from routes import (
    utill,
    default
)

app = FastAPI()

allow_origin = [
  "http://localhost:3000",
  "http://localhost:8000",
  "https://www.white-win.dev"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(utill.router)
app.include_router(default.router)
