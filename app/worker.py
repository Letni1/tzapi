import asyncio
from app.core.date import parse_date, date_range_list, date_to_nbu, date_to_datetime
from app.core.utils import get_data_json
from app.core.celery import celery_app
from app.crud.stats import insert_if_not_exist, bulk_insert_if_not_exist
from app.mongo.mongodb import MongoClient, get_db
from app.core.config import NBU_STAT_URL, MONGODB_URL


@celery_app.task
def add_stats_to_mongodb(
        start_date: int,
        end_date: int,
        db: MongoClient = MongoClient(MONGODB_URL)):
    print('started')
    start_date = parse_date(start_date)
    end_date = parse_date(end_date)
    date_list = date_range_list(start_date, end_date)
    for date in date_list:
        date = date_to_nbu(date)
        stats = get_data_json(url=NBU_STAT_URL+f'?date={date}&json')
        for stat in stats:
            stat['exchangedate'] = date_to_datetime(stat['exchangedate'])
        bulk_insert_if_not_exist(db, stats)
