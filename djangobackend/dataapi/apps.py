from django.apps import AppConfig
from django.core.cache import cache
import os
from pathlib import Path

class DataapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dataapi'

    def ready(self):
        print("============= execution ============")
        logspath = os.path.join(Path(__file__).resolve().parent, "data", "logs")
        logs_streams= {filename: "0" for filename in os.listdir(logspath)}
        redis_client = cache.client.get_client()
        if not redis_client.hgetall("logs_streams"):
            redis_client.hset("logs_streams", mapping=logs_streams)
       

