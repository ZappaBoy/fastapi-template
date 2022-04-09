from fastapi import APIRouter

from services.core import Core
from utils.logger import Logger

router = APIRouter()
core = Core()
logger = Logger('Api')


@router.get("/healthcheck")
def healthcheck():
    return {"Status": "Alive"}


@router.get("/test")
def test():
    status = core.test()
    return {"Status": status}
