import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import api
from utils.list_string_flattening_middleware import QueryStringFlatteningMiddleware

load_dotenv()

STATIC_FILES_PATH = "/engine"
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(",")

# Doc: http://127.0.0.1:80/redoc
app = FastAPI(
    title="Better Sports Bettor",
    description="BSB - Better Sports Bettor",
    version="0.1",
)

app.add_middleware(CORSMiddleware, allow_origins=ALLOWED_HOSTS)
app.add_middleware(QueryStringFlatteningMiddleware)

app.include_router(
    api.router,
    prefix="/api",
    tags=["api"])
