from fastapi import APIRouter
from fastapi import status
from starlette.responses import Response

from services.core import Core
from utils.logger import Logger

router = APIRouter()
core = Core()
logger = Logger('Api')


@router.get("/healthcheck")
def healthcheck():
    return {"Status": "Alive"}
