from app.mongo.mongodb import MongoClient
from pymongo import UpdateOne
from app.core.config import mongo_db_name, exchange_collection_name


def insert_if_not_exist(conn: MongoClient, data: dict):
    conn[mongo_db_name][exchange_collection_name].update_one(data, {'$set': data}, upsert=True)


def bulk_insert_if_not_exist(conn: MongoClient, data: list):
    conn[mongo_db_name][exchange_collection_name].bulk_write(
        [UpdateOne(stat, {'$set': stat}) for stat in data]
    )

