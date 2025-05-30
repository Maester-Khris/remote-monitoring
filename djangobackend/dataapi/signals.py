from django.apps import AppConfig
from django.core.cache import cache

class DataApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name="dataapi"

    def ready(self):
        print("============= execution ============")
        if not cache.hgetall("logs_streams"):
            cache.hset("logs_stream",mapping={})