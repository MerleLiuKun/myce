"""
    通用的配置文件
"""
from environs import Env

env = Env()
env.read_env()

# Celery 配置
RABBITMQ_HOST = env.str("RABBITMQ_HOST", "127.0.0.1")
RABBITMQ_VIRTUAL_HOST = env.str("RABBITMQ_VIRTUAL_HOST", "tests")

# redis
REDIS_HOST = env.str("REDIS_HOST", "127.0.0.1")
REDIS_PORT = env.int("REDIS_PORT", 6379)
CE_REDIS_DB = env.int("CE_REDIS_DB", 0)

try:
    from local_settings import *
except ImportError:
    pass
