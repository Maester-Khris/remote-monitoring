from pathlib import Path
import os
import json
import random

DATA_DIR = Path(__file__).resolve().parent.parent
datapath = os.path.join(DATA_DIR, "data", "todos.json")

def load_data():
    """Loads the data from the JSON file."""
    with open(datapath, 'r') as file:
        return json.load(file)

def data_producer():
    """Chooses a random object from the loaded data."""
    data = load_data()  # Load data on each call
    todo_user = random.choice(data) #use random.choice for better readability
    print(f"selected todo, {todo_user}")
    return todo_user