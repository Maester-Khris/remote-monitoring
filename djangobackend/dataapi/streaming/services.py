from pathlib import Path
import os
import json
import random
from concurrent.futures import ThreadPoolExecutor

DATA_DIR = Path(__file__).resolve().parent.parent
datapath = os.path.join(DATA_DIR, "data", "logs")

def read_file_in_chunk(filepath, chunk_size):
    chunks = []
    with open(filepath, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            chunks.append(chunk)
    return chunks

def load_data():
    chunk_size = 1024 * 1024
    logs_files = [filename for filename in os.listdir(datapath)]
    logs_file_path = [os.path.join(datapath, f) for f in logs_files]
    result = {}

    #parrallel files readding
    with ThreadPoolExecutor() as executor:
        future_to_file = {executor.submit(read_file_in_chunk, path, chunk_size): fname for path, fname in zip(logs_file_path, logs_files)}

        for future in future_to_file:
            fname = future_to_file[future]
            result[fname] = future.result()

    return result

def data_producer():
    """Chooses a random object from the loaded data."""
    data = load_data()  # Load data on each call
    print(data.keys())
    todo_user = random.choice(data.values) #use random.choice for better readability
    print(f"selected todo, {todo_user}")
    return todo_user