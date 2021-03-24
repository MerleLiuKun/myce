import config

# RabbitMQ management
broker_api = f"http://guest:guest@{config.RABBITMQ_HOST}:15672/api/"

# view address
address = "0.0.0.0"
port = 9999

# basic_auth now not work. reason checking.
basic_auth = ["guest:guest"]

# 持久化
persistent = True
db = "flower_db"
