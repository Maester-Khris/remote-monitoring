from pathlib import Path
import os
import json
import random
from concurrent.futures import ThreadPoolExecutor
from itertools import cycle

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
    data = load_data()
    if not data:
        return

    # Create an iterator of (filename, line) for each file
    file_iterators = []
    for filename, chunks in data.items():
        lines = []
        for chunk in chunks:
            try:
                text = chunk.decode("utf-8", errors="ignore")
                lines.extend(filter(None, text.strip().split("\n")))
            except Exception:
                continue
        file_iterators.append((filename, iter(lines)))

    # Interleave lines from all iterators
    iterators = [(fname, it) for fname, it in file_iterators if it]

    while iterators:
        still_active = []
        for fname, it in iterators:
            try:
                yield fname, next(it)
                still_active.append((fname, it))  # keep this one
            except StopIteration:
                continue  # this file is exhausted
        iterators = still_active  # remove exhausted ones











#     data = load_data()  
#     if not data:
#         return 
    
#     file_iterators = []
#     for filename, chunks in data.items():
#         lines = []
#         for chunk in chunks:
#             try:
#                 text = chunk.decode("utf-8", errors="ignore")
#                 lines.extends(filter(None, text.strip().split("\n")))
#             except Exception:
#                 continue
            
#             # for line in filter(None, text.strip().split("\n")):
#             #     yield filename, line

#         file_iterators.append((filename, iter(lines)))

#     # Interleave lines from all iterators
#     iterators = [(fname, it) for fname, it in file_iterators if it]

#     while iterators:
#         still_active = []
#         for fname, it in iterators:
#             try:
#                 yield fname, next(it)
#                 still_active.append((fname, it))  # keep this one
#             except StopIteration:
#                 continue
#         iterators = still_active


# all_chunks = [chunk for chunks in data.values() for chunk in chunks]
# if not all_chunks:
#     return {"error": "no data"}

# chunk = random.choice(all_chunks)

# all_lines = []
# for chunk in all_chunks:
#     try:
#         text = chunk.decode('utf-8', errors='ignore')
#         lines = text.strip().split("\n")
#         all_lines.extend(lines)
#     except Exception as e:
#         continue

# #print(all_lines[:3])
# if not all_lines:
#     return {"error": "no valid lines in logs"}

# return all_lines