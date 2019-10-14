from celery import Celery
from app.core.config import BROKER_URL, REDIS_URL

celery_app = Celery('worker', backend=REDIS_URL, broker=BROKER_URL)

celery_app.conf.task_routes = {'app.worker.add_stats_to_mongodb': 'main-queue'}