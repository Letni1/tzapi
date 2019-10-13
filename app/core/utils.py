from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from starlette.responses import JSONResponse
import json
import requests


def create_aliased_response(model: BaseModel) -> JSONResponse:
    return JSONResponse(content=jsonable_encoder(model, by_alias=True))


def get_data_json(url: str) -> json:
    r = requests.get(url)
    return r.json()
