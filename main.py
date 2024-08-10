import json
import os

# File path for the JSON file
FILE_PATH = "tasks.json"

# Load tasks from JSON file
def load_tasks():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    task_name = input("Enter the task description: ")
    tasks.append({"task": task_name, "completed": False})
    save_tasks(tasks)
    print(f"Task '{task_name}' added.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for index, task in enumerate(tasks, 1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{index}. {task['task']} [{status}]")

# Mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_index]['task']}' marked as completed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{removed_task['task']}' deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Main CLI loop
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
