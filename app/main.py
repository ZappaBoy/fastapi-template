import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse, RedirectResponse

import api
from utils.list_string_flattening_middleware import QueryStringFlatteningMiddleware

load_dotenv()
dirname = os.path.dirname(__file__)

STATIC_FILES_PATH = os.path.join(dirname, 'static')
STATIC_FILES_ENDPOINT = '/static'
FAVICON_PATH = os.path.join(STATIC_FILES_PATH, '/favicon/favicon.ico')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')

# Doc: http://127.0.0.1:YOUR_PORT/redoc
app = FastAPI(
    title='FastAPI Template',
    description='FastAPI Template',
    version='0.1'
)

app.add_middleware(CORSMiddleware, allow_origins=ALLOWED_HOSTS)
app.add_middleware(QueryStringFlatteningMiddleware)
app.mount(STATIC_FILES_ENDPOINT, StaticFiles(directory=STATIC_FILES_PATH, html=True), name=STATIC_FILES_PATH)

app.include_router(
    api.router,
    prefix='/api',
    tags=['api'])


@app.get('/', include_in_schema=False)
async def redirect():
    response = RedirectResponse(url=STATIC_FILES_ENDPOINT)
    return response


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(FAVICON_PATH)
