from pathlib import Path
import os
def readfileandfolder():
    path = Path('')
    items = list(path.glob('*'))
    for i, j in enumerate(items,1):
        print(f"{i} : {j}")
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
            print("No such file exists.")
    except Exception as err:
        print(f"An error occured as {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Enter file name to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
        else:
            print("No such file exists.")
    except Exception as err:
        print(f"An error occured as {err}")

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")
try:
    option = int(input("Enter your option(1, 2, 3, 4): "))
except:
    print("Invalid option.You have to select in the options above.")
if option == 1:
    createfile()
if option == 2:
    readfile()
if option == 3:
    updatefile()
if option == 4:
    deletefile()
