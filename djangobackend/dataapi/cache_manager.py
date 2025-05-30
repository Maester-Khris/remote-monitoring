import os
import django
from django.core.cache import cache

def write_to_logs_stream(subkey, value):
    cache.hset('logs_streams', subkey, value)

def read_from_logs_stream(subkey):
    return cache.hget('logs_streams', subkey)