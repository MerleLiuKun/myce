"""
    通用的配置文件
"""

# Celery 配置
RABBITMQ_HOST = "127.0.0.1"
RABBITMQ_VIRTUAL_HOST = "tests"

# redis
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
MQ_REDIS_DB = 0

try:
    from local_settings import *
except ImportError:
    pass
