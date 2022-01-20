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


@router.get("/top-player-in-teams")
def analyze_keywords(response: Response):
    response.status_code = status.HTTP_200_OK
    return {'API': 'OK'}
