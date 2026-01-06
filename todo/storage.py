import json
from pathlib import Path

DATA_FILE = Path("./data/tasks.json")

def load_tasks():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    DATA_FILE.parent.mkdir(exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)