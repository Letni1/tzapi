import requests
from typing import List
import json
from fastapi import APIRouter, Depends, HTTPException
from app.db_models.user import User as DBUser
from app.api.utils.security import get_current_active_user
from app.models.stats import Stats


router = APIRouter()
@router.get('/stats/')
def get_stats(date: int = None,
              current_user: DBUser = Depends(get_current_active_user)
) -> List:
    """
    Get stats for today
    """
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    if date:
        url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={}&json'.format(date)
    r = requests.get(url)
    stats = r.json()
    return stats
