from celery import Celery
from app.core.config import BROKER_URL, REDIS_URL

celery_app = Celery('worker', backend=REDIS_URL, broker=BROKER_URL)
