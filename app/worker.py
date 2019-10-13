from app.core.celery import celery_app


@celery_app.task
def test_celery(word):
    return f'test  celery {word}'
