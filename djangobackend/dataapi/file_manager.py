import os
def read_log_chunks(filepath, position, chunk_size=4096):
    try:
        with open(filepath, 'r') as f:
            f.seek(position)
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                yield {'data': chunk, 'newposition': f.tell()}
    except FileNotFoundError:
        yield {'data': "", 'newposition': 0}

def get_line_results(chunk_results):
    position = 0
    for chunk in chunk_results:
        position = chunk["newposition"]
        lines = chunk["data"].split("\n")
        for line in lines:
            if line:  # Avoid yielding empty lines
                yield {"line": line, "position": position}
        if position > 20000:
            break

# Example usage (for testing)
for line_result in get_line_results(read_log_chunks("/content/https_logs.txt", 0)):
    print(line_result)

