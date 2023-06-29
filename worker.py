import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

celery_worker = Celery(__name__)
celery_worker.conf.broker_url = os.environ.get("CELERY_BROKER_URL", 'redis://localhost:6379')
celery_worker.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", 'redis://localhost:6379')
celery_worker.conf.accept_content = ['application/json', ]


@celery_worker.task(name='fc')
def create_task(a: int, b: int) -> str:
    return {'result': a + b}
