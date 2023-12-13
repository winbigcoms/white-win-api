import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
import uvicorn
from dotenv import load_dotenv
from pathlib import Path
from routes import (
    utill,
    default
)

load_dotenv('.env')
ppem = os.environ.get('ppem')
fpem = os.environ.get('fpem')

app = FastAPI()

allow_origin = [
  "http://localhost:3000",
  "http://localhost:8000",
  "https://www.white-win.dev"
]

app.add_middleware(HTTPSRedirectMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(utill.router)
app.include_router(default.router)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        ssl_keyfile=ppem,
        ssl_certfile=fpem,
    )