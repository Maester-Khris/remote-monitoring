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
    data = load_data()  
    all_chunks = [chunk for chunks in data.values() for chunk in chunks]
    if not all_chunks:
        return {"error": "no data"}

    chunk = random.choice(all_chunks)

    all_lines = []
    for chunk in all_chunks:
        try:
            text = chunk.decode('utf-8', errors='ignore')
            lines = text.strip().split("\n")
            all_lines.extend(lines)
        except Exception as e:
            continue

    print(all_lines[:3])
    if not all_lines:
        return {"error": "no valid lines in logs"}

    return all_lines
   
    # try:
    #     text = chunk.decode('utf-8', errors='ignore')
    #     print(text)
    #     lines = text.strip().split("\n")
    #     json_lines = []
    #     return random.choice(lines)

    # except Exception as e:
    #     return {"error": f"failed to parse chunk: {str(e)}"}


    # for line in text:
    #     print(line)
    #     line = line.strip()
    #     if line:
    #         try:
    #             json_obj = json.loads(line)
    #             json_lines.append(json_obj)
    #         except json.JSONDecodeError:
    #             continue

    # print(json_lines)
    # if not json_lines:
    #     return {"error": "no valid JSON objects in chunk"}


    # print(data.keys())
    # todo_user = random.choice(list(data.values())) #use random.choice for better readability
    # print(f"selected todo, {todo_user}")
    # return todo_user