import random
import string

def generate_large_log_file(filename, num_lines, line_length=100):
    """Generates a large log file with random log entries."""

    with open(filename, 'w') as f:
        for _ in range(num_lines):
            log_entry = ''.join(random.choices(string.ascii_letters + string.digits + " ", k=line_length))
            f.write(log_entry + '\n')

# Generate a 1 million line log file (adjust as needed)
generate_large_log_file("https_logs.txt", 1000000)
print("Large log file 'https_logs.txt' generated.")