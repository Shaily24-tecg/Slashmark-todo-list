import json
import os

TASK_FILE = "tasks.json"
tasks = []

def load_tasks():
    global tasks
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            tasks = json.load(f)

def save_tasks():
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def display_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\n===== TO-DO LIST =====")
        for i, task in enumerate(tasks, start=1):
            status = "✓ Done" if task["completed"] else "✗ Pending"
            print(f"{i}. {task['task']} - {status}")

def add_task(task_name):
    tasks.append({"task": task_name, "completed": False})
    save_tasks()
    print("Task added successfully!")

def mark_completed(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks()
        print("Task marked as completed!")
    else:
        print("Invalid task number!")

def remove_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        save_tasks()
        print(f"Removed: {removed['task']}")
    else:
        print("Invalid task number!")

load_tasks()

while True:
    print("\n===== MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Completed")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_tasks()

    elif choice == "2":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "3":
        display_tasks()
        mark_completed(int(input("Task number: ")))

    elif choice == "4":
        display_tasks()
        remove_task(int(input("Task number: ")))

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")