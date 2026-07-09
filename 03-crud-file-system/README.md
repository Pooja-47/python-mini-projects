# 📁 CRUD File System

A menu-driven Python application that performs **CRUD (Create, Read, Update, Delete)** operations on files. This project was built to strengthen my understanding of **Python File Handling**, **Exception Handling**, **Modules**, and **Pathlib** while following a modular programming approach.

---

## ✨ Features

- 📄 Create a new file
- 📖 Read file contents
- ✏️ Update existing files
  - Rename file
  - Append new content
  - Overwrite existing content
- 🗑️ Delete files
- 📝 Automatically log all file operations with timestamps
- ⚠️ Exception handling for common file-related errors
- 📂 Modular project structure

---

## 🛠️ Technologies Used

- Python 
- File Handling
- Exception Handling
- Pathlib
- Modular Programming

---

## 📂 Project Structure

```text
03-crud-file-system/
│
├── main.py              # Entry point of the application
├── file_ops.py          # CRUD operations and activity logging
├── utils.py             # Helper functions
├── activity_log.txt     # Generated automatically after running
└── README.md
```

---

## 📝 Sample Activity Log

```text
2026-07-09 20:15:10 | CREATED | notes.txt
2026-07-09 20:16:05 | READ | notes.txt
2026-07-09 20:17:32 | APPENDED | notes.txt
2026-07-09 20:18:14 | RENAMED | notes.txt -> python_notes.txt
2026-07-09 20:19:42 | DELETED | python_notes.txt
```

---

## 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/python-mini-projects.git
```

### 2️⃣ Navigate to the project folder

```bash
cd python-mini-projects/03-crud-file-system
```

### 3️⃣ Run the application

```bash
python main.py
```

---

## 📋 Menu Options

```text
===== FILE SYSTEM MENU =====

C - Create File
R - Read File
U - Update File
D - Delete File
Q - Quit
```

---

## 📌 Concepts Practiced

- Functions
- Modules
- File Handling
- Exception Handling
- Pathlib
- File Validation
- CRUD Operations
- Logging
- Modular Project Organization

---


## 🎯 Learning Outcomes

Through this project, I learned how to:

- Design a menu-driven CLI application
- Organize code using multiple Python modules
- Perform safe file operations
- Handle exceptions effectively
- Record application activity using log files
- Build a reusable and maintainable project structure

---

## 🔮 Future Improvements

- Search files by keyword
- List all available files
- JSON-based activity logs
- Analytics dashboard
- Object-Oriented Programming (OOP) version
- Graphical User Interface (GUI)

---

## 👩‍💻 Author

**Pooja Kanwar**

B.Tech CSE Student | Python Learner | Aspiring Data Engineer

GitHub: https://github.com/Pooja-47