import shutil
import os


FOLDERPATH = r"C:\Users\27Obarkham\Desktop\Python programs\lessons\python_24feb"
from anyio import open_file
os.system("cls")
terminal_size = shutil.get_terminal_size()
width = terminal_size.columns
def menu():
    print("---------MENU---------\n".center(width))
    print("A: NewFile".center(width))
    print("B: EditFile".center(width))
    print("C: DeleteFile".center(width))
    print("D: ReadFile".center(width))
    print("E: Exit".center(width))
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
        exit()
    else:
        print("Invalid choice")

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
    name = name + ".txt"
    file_path = os.path.join(folder_path, name)

    with open(file_path, "w") as file:
        text = input("Enter text: ")
        file.write(text)
   
    print(f"File '{name}' has been created in '{folder_path}'.")

    menu()

def EditFile():
    print ("editing...")

def DelFile():
    os.system("cls")
    for files in os.walk(r"C:\Users\27Obarkham\Desktop\Python programs\lessons\python_24feb"):
        for file in files:
            print(file)
    file = input("Enter file name to delete: ")
    file = file + ".txt"
    folder_path = r"C:\Users\27Obarkham\Desktop\Python programs\lessons\python_24feb"
    file_path = os.path.join(folder_path, file)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file}' has been deleted.")
    else:
        print(f"File '{file}' does not exist.")
   
    menu()

def ReadFile():
    file = input("What is the name of your file(excluding .txt): ")
    file = file + ".txt"

    print ("hello world")

menu()

