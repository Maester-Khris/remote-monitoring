import sys
from django.apps import AppConfig
from django.core.cache import cache
import os
from pathlib import Path

class DataapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dataapi'

    def ready(self):
        # Determine if a management command is running that shouldn't touch Redis
        # Note: sys.argv[1] is typically the command name (e.g., 'runserver', 'collectstatic')
        # Check against the second argument (the actual command) for more robustness
        is_management_command = len(sys.argv) > 1 and sys.argv[1] in [
            'makemigrations',
            'migrate',
            'collectstatic',
            'test', # Often you don't want Redis connections during tests either
            'check', # Or health checks
        ]

        # Use an environment variable for explicit control during build/testing
        skip_redis_connect = os.environ.get('DJANGO_SETTINGS_SKIP_REDIS_CONNECT') == '1'

        if not is_management_command and not skip_redis_connect:
            try:
                print("============= attempting connection to redis ============") # More descriptive message
                # Ensure the path is correct within the Docker container context
                # If your project structure is /app/djangobackend/dataapi/apps.py
                # And logs are in /app/data/logs
                # You might need to adjust the path based on your project structure and Dockerfile COPY
                # A safer way to get project root is to pass BASE_DIR from settings:
                # from django.conf import settings
                # logspath = os.path.join(settings.BASE_DIR, "data", "logs")
                
                # For now, assuming current path relative to apps.py is correct
                logspath = os.path.join(Path(__file__).resolve().parent, "data", "logs")

                # Ensure the logs directory exists and is readable, otherwise os.listdir will fail
                if not os.path.isdir(logspath):
                    print(f"Warning: Log directory '{logspath}' not found. Skipping Redis log stream setup.")
                    return # Exit early if directory isn't there

                logs_streams = {filename: "0" for filename in os.listdir(logspath)}

                # Attempt to get the redis client via Django's cache system
                redis_client = cache.client.get_client()

                # Ping Redis to verify connection before attempting operations
                redis_client.ping() # This will raise an exception if connection fails

                if not redis_client.hgetall("logs_streams"):
                    redis_client.hset("logs_streams", mapping=logs_streams)
                    print("============= Redis logs_streams initialized ============")
                else:
                    print("============= Redis logs_streams already exists ============")

            except Exception as e:
                print(f"ERROR: Could not initialize Redis for logs_streams: {e}")
                # Consider if this is a fatal error or just a warning for your app.
                # If it's fatal, re-raise it: raise e
                # If it's non-fatal during build, just log.       

