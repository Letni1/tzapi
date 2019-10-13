from datetime import datetime
from typing import List
from pydantic import BaseModel


class StatsBase(BaseModel):
    r030: str
    txt: str
    rate: float
    cc: str
    exchangedate: datetime


class StatsInDB(StatsBase):
    pass


class Stats(StatsInDB):
    pass


class StatsInResponse(BaseModel):
    stats: List[Stats]
