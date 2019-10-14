from datetime import datetime
from typing import Optional, List
import pandas as pd
import requests
import re


def parse_date(date: int) -> str:
    pattern = re.compile(r'\d{1,4}(?=(\d{2}))')
    result = pattern.sub(r'\g<0>-', str(date))
    return result


def date_to_datetime(date: str) -> datetime:
    date = pd.to_datetime(date).to_pydatetime()
    return date


def date_range_list(date1: str, date2: str) -> List[datetime]:
    date_list = pd.date_range(date1, date2).tolist()
    return date_list


def date_to_nbu(date: datetime) -> str:
    date_str = str(date.date())
    date_nbu = ''.join(date_str.split('-'))
    return date_nbu

