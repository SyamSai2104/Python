tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "completed": status == "True"})
    except FileNotFoundError:
        pass

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(f"{task['task']}|{task['completed']}\n")

def add_task():
    task_name = input("Enter task: ").strip()
    tasks.append({"task": task_name, "completed": False})
    print("----------*----------")
    print(f"Added: '{task_name}'")
    print("----------*----------")

def view_tasks():
    if not tasks:
        print("----------*----------")
        print("No tasks!")
        print("----------*----------")
        return
    
    print("\n--- YOUR TASKS ---")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['task']}")
        print("----------*----------")

# ... (other functions)
def complete_task():
    view_tasks()
    try:
        idx = int(input("Enter task number to complete: ")) - 1
        tasks[idx]["completed"] = True
        print(f"Marked as complete!")
    except (IndexError, ValueError):
        print("Invalid task number")

def delete_task():
    view_tasks()
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(idx)
        print("----------*----------")
        print(f"Deleted: '{removed['task']}'")
        print("----------*----------")
    except (IndexError, ValueError):
        print("----------*----------")
        print("Invalid task number")
        print("----------*----------")

def main():
    load_tasks()
    
    while True:
        print("\n==== TO-DO LIST ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        print("----------*----------")
        
        choice = input("Choose an option (1-5): ")
        
        actions = {
            "1": add_task,
            "2": view_tasks,
            "3": complete_task,
            "4": delete_task,
            "5": lambda: exit(save_tasks())
        }
        
        if choice in actions:
            actions[choice]()
        else:
            print("----------*----------")
            print("Invalid choice. Try 1-5.")

if __name__ == "__main__":
    main()