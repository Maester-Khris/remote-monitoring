import asyncio
import random
import time
import json

from django.http import StreamingHttpResponse
from django.shortcuts import render
from .services import data_producer

async def sse_stream(request):
    """
    Sends server-sent events to the client during 2min.
    """
    async def event_stream():
        stop_at = time.time() + 120 # duration in seconds

        while time.time()<stop_at:
            for filename, line in data_producer():
                json_data = json.dumps({"filename":filename, "log":line})
                yield f"data: {json_data}\n\n"
                await asyncio.sleep(1)
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')

# all_lines = data_producer()  # returns the full list now
# for line in all_lines:
#     json_data = json.dumps({"log": line})
#     yield f"data: {json_data}\n\n"
#     await asyncio.sleep(1)  # control flow to simulate live feed

#=========== Old ============
# todo_user = data_producer()
# #print(todo_user)
# json_data = json.dumps(todo_user)
# yield f'data: {json_data}\n\n'
# await asyncio.sleep(1)