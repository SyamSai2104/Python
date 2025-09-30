from pathlib import Path
import os
def readfileandfolder():
    path = Path('.')
    items = list(path.iterdir())
    
    if not items:
        print("No files or folders found.")
        return
    
    print("\nFiles and folders in current directory:")
    for i, item in enumerate(items, 1):
        item_type = "📁" if item.is_dir() else "📄"
        print(f"{i:2d} : {item_type} {item.name}")
def createfile():
    try:
        readfileandfolder()
        name = input("Enter file name: ")
        p = Path(name)
        if p.exists():
            print("File already exists")
        else:
            with open(p,'w') as ps:
                data = input("Enter what you want to write in file: ")
                ps.write(data)
            print("File created succesfully")
    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Enter file name to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fi:
                data = fi.read()
                print(data)
        else:
            print("File doesnot exist.")
    except Exception as err:
        print(f"Error occured {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Enter the file name you want to update: ")
        p = Path(name)

        if p.exists() and p.is_file():
            print("Press 1 for changing file name: ")
            print("Press 2 for overwriting content in the file: ")
            print("Press 3 for adding content in your file: ")

            res = int(input("Your response: "))
            
            if res == 1:
                name2 = input("Enter your new file name: ")
                p2 = Path(name2)
                p.rename(p2)
                
            elif res == 2:
                with open(p,'w') as fi:
                    data = input("Enter what you want to override: ")
                    fi.write(data)
                    
            elif res == 3:
                with open(p, 'a') as fi:
                    data = input("Enter your content to add to the file: ")
                    fi.write(data)
            else:
                print("invalid option.")
        else:
            print("No such file.")
    except Exception as err:
        print(f"An error occured as {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Enter file name to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").lower()
            if confirm == 'y':
                p.unlink()
                print("File deleted successfully")
            else:
                print("Deletion cancelled")
        else:
            print("No such file exists.")
    except Exception as err:
        print(f"An error occurred: {err}")

def main_menu():
    while True:
        print("\n=== File Management System ===")
        print("1. Create a file")
        print("2. Read a file")
        print("3. Update a file")
        print("4. Delete a file")
        print("5. Exit")
        
        try:
            option = int(input("Enter your option (1-5): "))
            if option == 1:
                createfile()
            elif option == 2:
                readfile()
            elif option == 3:
                updatefile()
            elif option == 4:
                deletefile()
            elif option == 5:
                print("Goodbye!")
                break
            else:
                print("Please enter a number between 1-5")
        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    main_menu()