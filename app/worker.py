import asyncio
from app.core.date import parse_date, date_range_list, date_to_nbu
from app.core.utils import get_data_json
from app.core.celery import celery_app
from app.crud.stats import insert_if_not_exist
from app.mongo.mongodb import AsyncIOMotorClient, get_db


@celery_app.task
def test_celery(word):
    return f'test  celery {word}'


@celery_app.task
def add_stats_to_mongodb(
        start_date: int,
        end_date: int,
        db: AsyncIOMotorClient = get_db):
    start_date = parse_date(start_date)
    end_date = parse_date(end_date)
    date_list = date_range_list(start_date, end_date)
    try:
        for date in date_list:
            date = date_to_nbu(date)
            stat = get_data_json(date)
            asyncio.run(insert_if_not_exist(db, stat))
    except Exception as e:
        print(e.message)
