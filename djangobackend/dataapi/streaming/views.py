import asyncio
import os
import time
import json

from pathlib import Path
from django.shortcuts import render
from django.http import StreamingHttpResponse
from .services import LogTailer, data_producer

DATA_DIR = Path(__file__).resolve().parent.parent
datapath = os.path.join(DATA_DIR, "data", "logs")

log_tailer = LogTailer(directory=datapath)


async def event_stream():
    while True:
        for fname, line in log_tailer.generate_interleaved_lines():
            data = {"filename": fname, "log": line}
            yield f"data: {json.dumps(data)}\n\n"
            await asyncio.sleep(1)  # Throttle each message

        await asyncio.sleep(1)  # Delay between polling for new log updates

def stream_logs(request):
    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")


# ================================== Old code ===================================
# Notes: Still working, moved on to a new paradigm

async def sse_stream_old(request):
    """
    -- Sends server-sent events to the client during 2min.
    -- duration based: send only content between a predi
    """
    async def event_stream():
        stop_at = time.time() + 120 # duration in seconds

        while time.time()<stop_at:
            for filename, line in data_producer():
                json_data = json.dumps({"filename":filename, "log":line})
                yield f"data: {json_data}\n\n"
                await asyncio.sleep(1)
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')



#============================ Old =============================
#===== Notes: returning logs lines without files indications
# all_lines = data_producer()  # returns the full list now
# for line in all_lines:
#     json_data = json.dumps({"log": line})
#     yield f"data: {json_data}\n\n"
#     await asyncio.sleep(1)  # control flow to simulate live feed

