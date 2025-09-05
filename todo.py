import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\nOptions: add / view / delete / exit")
        choice = input("Enter choice: ").strip().lower()

        if choice == "add":
            task = input("Enter task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print(f"Task '{task}' added.")
        elif choice == "view":
            show_tasks(tasks)
        elif choice == "delete":
            show_tasks(tasks)
            try:
                idx = int(input("Enter task number to delete: ")) - 1
                if 0 <= idx < len(tasks):
                    removed = tasks.pop(idx)
                    save_tasks(tasks)
                    print(f"Task '{removed}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
