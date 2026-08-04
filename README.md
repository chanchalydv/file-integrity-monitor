# 🔐 File Integrity Monitor

A beginner-friendly cybersecurity project built with Python that detects unauthorized changes to files using **SHA-256 hashing**.

---

## 📌 About the Project

The **File Integrity Monitor (FIM)** scans files inside a monitored directory and creates a unique SHA-256 hash for each file.

During the next scan, the program calculates the hash again and compares it with the previously stored hash.

If the hash is different, the file has been modified.

The system can detect:

- 🆕 New files
- ✏️ Modified files
- 🗑️ Deleted files
- ✅ Unchanged files

It also maintains an activity log and stores file hashes in a JSON database.

---

## 🎯 Project Objective

The main objective of this project is to understand how **file integrity monitoring** works in cybersecurity.

It demonstrates how hashing can be used to detect unauthorized modifications to important files.

---

## 🛠️ Technologies Used

- 🐍 Python
- 🔐 SHA-256
- 📄 JSON
- 📁 File System Operations
- `hashlib`
- `os`
- `datetime`

---

## 📂 Project Structure

```text
file-integrity-monitor/
│
├── monitor.py
├── database.json
├── logs.txt
├── README.md
├── .gitignore
│
├── screenshots/
│   └── Desktop file integrity monitor screenshot.png
│
└── monitored_files/
    ├── test.txt
    └── important.txt
