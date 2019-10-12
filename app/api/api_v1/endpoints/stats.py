import requests
from typing import List, Optional
import json
from fastapi import APIRouter, Depends, HTTPException
from app.db_models.user import User as DBUser
from app.api.utils.security import get_current_active_user
from app.crud.exchange import insert_if_not_exist
from app.core.utils import create_aliased_response, date_to_isodate
from app.mongo.mongodb import AsyncIOMotorClient, get_db


router = APIRouter()


@router.get('/exchange/')
async def get_exchange(date: Optional[int] = None,
                       db: AsyncIOMotorClient = Depends(get_db),
                       current_user: DBUser = Depends(get_current_active_user)
                       ):
    """
    Get stats for today
    """
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    if date:
        url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={}&json'.format(date)
    r = requests.get(url)
    stats = r.json()
    for stat in stats:
        stat['exchangedate'] = date_to_isodate(stat['exchangedate'])
        await insert_if_not_exist(db, stat)


