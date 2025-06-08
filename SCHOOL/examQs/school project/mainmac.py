import shutil
import os
import platform
import importlib

terminal_size = shutil.get_terminal_size()
width = terminal_size.columns

running = True

os_info = platform.system()

if os_info == "Darwin":
    FOLDERPATH = r"/Users/oliverbarkham/Documents/Python_programs/school project"
    CLEARSCREEN = "clear"
else:
    FOLDERPATH = r"C:\Users\27Obarkham\Desktop\Python programs\functionproject"
    CLEARSCREEN = "cls"

os.system(CLEARSCREEN)

def menu():
    print("---------MENU---------\n".center(width))
    print("A: NewFile".center(width))
    print("B: EditFile".center(width))
    print("C: DeleteFile".center(width))
    print("D: ReadFile".center(width))
    print("E: CreatePythonFile".center(width))
    print("Q: Quit".center(width))
    print("----------------------\n".center(width))

    choice = input("choice: ")
    choice = choice.capitalize()
    if choice == "A":
        NewFile()
    elif choice == "B":
        EditFile()
    elif choice == "C":
        DelFile()
    elif choice == "D":
        ReadFile()
    elif choice == "E":
        CreatePythonFile()
    elif choice == "Q":
        os.system(CLEARSCREEN)
        exit()
    else:
        print("Invalid choice")
        os.system(CLEARSCREEN)
        menu()

def NewFile():
    choice =  input("Would you like to create file in a specified path: ".center(width))
   
    if choice == "yes":
        folder_path = input("Enter folder path: ")
    else:
        folder_path = FOLDERPATH

    if not os.path.exists(folder_path):
        print("The specified folder does not exist. Please create it first.")
        return
   
    name = input("Enter file name: ")
    extension = str(input("Enter file extension: "))
    name = name + extension
    file_path = os.path.join(folder_path, name)

    with open(file_path, "w") as file:
        text = input("Enter text: ")
        file.write(text)
   
    print(f"File '{name}' has been created in '{folder_path}'.")


def EditFile():

    filename = input("What is the name of your file (excluding .txt): ")
    filename += ".txt"
    file_path = os.path.join(FOLDERPATH, filename)
    with open(file_path, "r") as file:
        content = file.read()
        print (f"Content:\n{content}")

    choice = input("Would you like to:\nAppend: A\nOverwrite: B\n").upper()
    if choice == "A":
        print (content)
        new = input("What would you like to input\n")
        with open(file_path, "a") as file:
            file.write(new)
        print("success")
    else:
        print(content)
        new = input("What would you like to overwrite with:\n")
        with open(file_path, "w") as file:
            file.write(new)

def DelFile():
    os.system(CLEARSCREEN)
    for root, dirs, files in os.walk(FOLDERPATH):
        for file in files:
            print(file)
    file = input("Enter file name to delete: ")
    file = file + ".txt"
    folder_path = FOLDERPATH
    file_path = os.path.join(folder_path, file)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file}' has been deleted.")
    else:
        print(f"File '{file}' does not exist.")
   
def CreatePythonFile():
    name = input("Enter file name: ")
    name = name + ".py"
    file_path = os.path.join(FOLDERPATH, name)
    with open(file_path, "w") as file:
        file.write("def main():\n")
        text = input("Enter text: ")
        file.write(text)
    print(f"File '{name}' has been created in '{FOLDERPATH}'.")

def ReadFile():
    file = input("What is the name of your file(excluding .txt): ")
    file = file + ".txt"
    file_path = os.path.join(FOLDERPATH, file)
    with open(file_path, "r") as file:
        for line in file:
            if line.strip() == "":
                continue
            else:
                print(line)

while running:
    menu()
