"""

"""
import time

from celery.exceptions import SoftTimeLimitExceeded, TimeLimitExceeded

from celery_entry import celery_app
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
def long_time_task_with_output(seconds=10):
    seconds = int(seconds)
    for idx in range(seconds):
        if idx % 5 == 0:
            logger.info(f"Now sleep at seconds: {idx}")
        time.sleep(1)
    return True


@celery_app.task(queue="test-queue", time_limit=10)
def long_time_task_limit(seconds=20):
    seconds = int(seconds)
    try:
        for idx in range(seconds):
            if idx % 5 == 0:
                logger.info(f"Now sleep at seconds: {idx}")
            time.sleep(1)
        return True
    except SoftTimeLimitExceeded:
        # Won't stop worker.
        logger.info(f"Sorry, we have soft task limit to 10s.")
        return False
    except TimeLimitExceeded:
        # Will stop worker and create new worker.
        logger.info(f"Sorry, we have task limit to 10s.")
        return False
