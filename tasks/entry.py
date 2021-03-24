"""

"""
import time

from celery_worker import celery_app
from tasks import logger


@celery_app.task(queue="test-queue")
def simple_task():
    return True


@celery_app.task(queue="test-queue")
def long_time_task(seconds=10):
    seconds = int(seconds)
    time.sleep(seconds)
    return True


@celery_app.task(queue="test-queue")
def long_time_task(seconds=10):
    seconds = int(seconds)
    for idx in range(seconds):
        if idx % 5 == 0:
            logger.info(f"Now sleep at seconds: {idx}")
        time.sleep(1)
    return True
