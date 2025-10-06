import json
from pathlib import Path
from task_manager_app.task import Task
DATA_FILE =Path("data/tasks.json")
def load_tasks():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            data =json.load(f)
            return [Task.from_dict(task) for task in data]
    return[]
def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)
