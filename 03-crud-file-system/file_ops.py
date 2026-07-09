from datetime import datetime
from pathlib import Path
import os

def log_action(action, filename):
    with open("activity_log.txt", "a") as log:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{time} | {action} | {filename}\n")

def createfile():
    try:
        fileName = input("Enter file name to create: ")
        path = Path(fileName)

        if path.exists():
            print("File already exists!")
            choice = input("Do you want to overwrite it? (y/n): ").lower()

            if choice != "y":
                print("File not created.")
                return

        data = input("Enter content for the file: ")

        with open(path, "w") as fs:
            fs.write(data)

        print("File created/updated successfully!")

        log_action("CREATED", fileName)

    except Exception as err:
        print(f"Error occurred: {err}")


def readfile():
    try:
        name = input("Enter file name to read: ")
        path = Path(name)

        if not path.exists():
            print("File does not exist!")
            return

        with open(path, "r") as fs:
            content = fs.read()

            if content.strip() == "":
                print("File is empty.")
                log_action("READ_EMPTY", name)
            else:
                print("\n===== FILE CONTENT =====")
                print(content)
                log_action("READ", name) 

    except Exception as err:
        print(f"Error occurred: {err}")


def updatefile():
    try:
        name = input("Enter file name to update: ")
        path = Path(name)

        if not path.exists():
            print("File does not exist!")
            return

        print("\nUpdate Options:")
        print("1. Rename file")
        print("2. Append content")
        print("3. Overwrite content")

        try:
            choice = int(input("Enter your choice (1/2/3): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            return

        if choice == 1:
            new_name = input("Enter new file name: ")
            new_path = Path(new_name)

            if new_path.exists():
                print("Error: A file with this name already exists.")
            else:
                path.rename(new_path)
                print("File renamed successfully!")

                log_action("RENAMED", f"{name} -> {new_name}")

        elif choice == 2:
            data = input("Enter text to append: ")
            with open(path, "a") as fs:
                fs.write("\n" + data)
            print("Content appended successfully!")

            log_action("APPENDED", name)

        elif choice == 3:
            data = input("Enter new content (this will overwrite): ")
            with open(path, "w") as fs:
                fs.write(data)
            print("File overwritten successfully!")
            
            log_action("OVERWRITTEN", name)   

        else:
            print("Invalid choice! Please select 1, 2, or 3.")

    except Exception as err:
        print(f"Error occurred: {err}")

                    
def deletefile():
    try:
        name = input("Tell the name of file you want to delete: ")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("Successfully deleted!")

            log_action("DELETED", name)
        else:
            print("The file name you gave does not exist.")
    except Exception as err:
        print(f"{err} occurred")




