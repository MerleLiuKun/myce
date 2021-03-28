"""
    Config for celery
"""
import config

# 中间人(Broker) 和 结果存储 (ResultEnd) 配置
broker_url = (
    f"pyamqp://guest:guest@{config.RABBITMQ_HOST}:5672/{config.RABBITMQ_VIRTUAL_HOST}"
)
result_backend = f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}/{config.CE_REDIS_DB}"

# 时区设置
enable_utc = True
timezone = "UTC"

# worker 设置
worker_concurrency = 1  # 并发的 worker
worker_prefetch_multiplier = 1  # 每次预取一个任务

# 超时设置
task_time_limit = None

# 为防止内存泄露，每个 worker 每执行 一批任务后 将会被销毁重建
worker_max_tasks_per_child = 100

# 任务的序列化 设置
accept_content = ["pickle", "json"]

# 导入任务
imports = [
    "tasks.entry"
]
