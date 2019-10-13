from app.mongo.mongodb import AsyncIOMotorClient
from app.core.config import mongo_db_name, exchange_collection_name


async def insert_if_not_exist(conn: AsyncIOMotorClient, data: dict):
    await conn[mongo_db_name][exchange_collection_name].update_one(data, {'$set': data}, upsert=True)
