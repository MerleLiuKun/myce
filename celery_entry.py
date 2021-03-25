"""
    App for celery
"""
import logging

import structlog
from celery import Celery

import celeryconfig
from utils.log_setup import setup_structlog

celery_app = Celery()
celery_app.config_from_object(celeryconfig)

setup_structlog()
logger = structlog.wrap_logger(logging.getLogger("celery"))
