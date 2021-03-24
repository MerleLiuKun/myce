import logging

import structlog

from utils.log_setup import setup_structlog

setup_structlog()
logger = structlog.wrap_logger(logging.getLogger("tasks"))
