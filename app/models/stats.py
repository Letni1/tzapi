from pydantic import BaseModel
from typing import List


class StatsBase(BaseModel):
    exchange: List[dict]


class StatsGet(StatsBase):
    date: int


class Stats(StatsGet):
    pass
