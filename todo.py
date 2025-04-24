import json
import os

TASKS_FILE = "todo.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE) or os.path.getsize(TASKS_FILE) == 0:
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)
    
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("Task Title can not be empty.")
        return
    
    new_id = 1 if not tasks else tasks[-1]["id"] + 1
    task ={
        "id": new_id,
        "title": title,
        "done": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {title}")


def view_task(tasks):
    if not tasks:
        print("No Tasks were found.")
        return
    
    print("\n To-Do List:")
    for task in tasks:
        status = "Finished" if task["done"] else "Incomplete"
        print(f"[{task['id']}] {status} {task['title']}")

def mark_done(tasks):
    try:
        task_id = int(input("Enter task ID to mark as Finished: "))
    except ValueError:
        print("Please enter a valid ID: ")
        return
    
    for task in tasks:
        if task["id"] == task_id:
            if task["done"]:
                print("Task is already marked as complete.")
            else:
                task["done"]=True
                save_tasks(tasks)
                print(f"Task [{task_id}] marked as complete.")
            return
    print(f"Task with ID [{task_id}] not found.")

def delete_task(tasks):
    try:
        task_id = int(input("Enter the Task ID you would like to remove: "))
    except ValueError:
        print("Please Enter a valid Task ID: ")
        return
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            confirm = input(f"Are you sure you would like to delete '{task['title']}'? (y/n: ").lower()
            if confirm == 'y':
                tasks.pop(i)
                save_tasks(tasks)
                print(f"Task [{task_id}] deleted.")
            else:
                print("Deletion Cancelled.")
            return
    print(f"❌ Task with ID [{task_id}] not found.")


def main():
    tasks = load_tasks()

    while True:
        print("\n ====== TO-DO MENU ======")
        print("1. View tasks")
        print("2. Add Task")
        print("3. Mark as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        match choice:
            case "1": 
                view_task(tasks)
            case "2": 
                add_task(tasks)
            case "3": 
                mark_done(tasks)
            case "4": 
                delete_task(tasks)
            case "5": 
                print("Goodbye!") 
                break
            case _:
                print("Invalid Input, Try Again: ")

if __name__ == "__main__":
    main()
