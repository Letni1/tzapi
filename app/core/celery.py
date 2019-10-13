from celery import Celery
from app.core.config import BROKER_URL, CELERY_RESULT_BACKEND

celery_app = Celery('worker', backend=CELERY_RESULT_BACKEND, broker=BROKER_URL)

