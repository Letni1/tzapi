import requests
from typing import List, Optional
import json
from fastapi import APIRouter, Depends, HTTPException
from app.db_models.user import User as DBUser
from app.api.utils.security import get_current_active_user
from app.crud.stats import insert_if_not_exist
from app.models.stats import StatsInResponse
from app.core.config import NBU_STAT_URL
from app.core.utils import create_aliased_response, get_data_json
from app.core.date import date_to_datetime
from app.mongo.mongodb import MongoClient, get_db


router = APIRouter()


@router.get('/stats/')
def get_exchange(
                       db: MongoClient = Depends(get_db),
                       current_user: DBUser = Depends(get_current_active_user)
                       ):
    """
    Get stats for today
    """
    url = NBU_STAT_URL + '?json'
    stats = get_data_json(url)
    for stat in stats:
        stat['exchangedate'] = date_to_datetime(stat['exchangedate'])
        insert_if_not_exist(db, stat)
    return create_aliased_response(StatsInResponse(stats=stats))

