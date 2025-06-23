tasks = []
def add_task():
    t = input(f"Enter your task: ")
    tasks.append(t)
    print(f"Task {t} added succefully")
            
def remove_task():
    t = input("Enter a task to remove: ")
    tasks.remove(t)
    print(f"Task {t} removed succefully")

def view_task():
    print()
    if not tasks:
        print("No tasks")
        return
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")
        

def main():
    print("Welcome to your daily To-Do-List")
    print()
    while True:
        print()
        print("Enter 1 to add a task")
        print("Enter 2 to remove a task")
        print("Enter 3 to see all tasks")
        print("Q to Quit")
        option = input().strip()

        if option.lower() == 'q':
            print("Have a good day")
            with open("mytodo.txt", 'w') as f:
                for i, t in enumerate(tasks, 1):
                    f.write(f"{i}. {t}\n")
            break
        elif option.isdigit():
            option = int(option)
            if option == 1:
                    add_task()
            elif option == 2:
                 remove_task()
            elif option == 3:
                view_task()
            else:
                print("Invalid Operator")
        else:
            print("Invalid option")
main()