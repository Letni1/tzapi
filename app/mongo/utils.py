import logging
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGODB_URL
from app.mongo.mongodb import db


async def connect_to_mongo():
    logging.info('Connecting to db')
    db.client = AsyncIOMotorClient(str(MONGODB_URL))
    logging.info("Connected to db")


async def close_mongo_connection():
    logging.info("Disconnecting from db")
    db.client.close()
    logging.info("Disconnected from db")

