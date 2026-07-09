from pathlib import Path

def list_files():
    files = list(Path(".").glob("*"))

    print("\n===== FILES IN DIRECTORY =====")
    found = False

    for file in files:
        if file.is_file():
            print(file.name)
            found = True

    if not found:
        print("No files found in directory.")

def search_file():
    name = input("Enter file name to search: ")
    path = Path(name)

    if path.exists():
        print(f"File found: {path.resolve()}")
    else:
        print("File not found.")