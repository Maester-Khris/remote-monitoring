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
    structure of a todo object: 
    {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": false
    }
    """
    async def event_stream():
        start_time = time.time()  # Record the start time
        end_time = start_time + 120

        while True:
            if time.time() >= end_time:
                break  # Exit the loop after 5 minutes
             
            todo_user = data_producer()
            json_data = json.dumps(todo_user)
            yield f'data: {json_data}\n\n'
            await asyncio.sleep(1)

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')
