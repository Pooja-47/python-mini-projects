from file_ops import createfile, readfile, updatefile, deletefile
from utils import list_files, search_file

while True:
    print("\n===== SMART FILE MANAGER =====")
    print("C - Create File")
    print("R - Read File")
    print("U - Update File")
    print("D - Delete File")
    print("L - List All Files")
    print("S - Search File")
    print("Q - Quit")

    operation = input("\nEnter your choice: ").lower()

    if operation == "c":
        createfile()

    elif operation == "r":
        readfile()

    elif operation == "u":
        updatefile()

    elif operation == "d":
        deletefile()

    elif operation == "l":
        list_files()

    elif operation == "s":
        search_file()

    elif operation == "q":
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
