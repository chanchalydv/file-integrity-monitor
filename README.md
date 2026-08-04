# 🔐 File Integrity Monitor

A beginner-friendly cybersecurity project built with Python that detects unauthorized changes to files using SHA-256 hashing.

## 📌 About the Project

The File Integrity Monitor (FIM) continuously checks files inside a monitored directory and creates a unique SHA-256 hash for each file.

During every scan, the newly calculated hash is compared with the previously stored hash.

If the hash changes, the program detects that the file has been modified.

The system can detect:

- 🆕 New files
- ✏️ Modified files
- 🗑️ Deleted files
- ✅ Unchanged files

It also maintains an activity log and stores file hashes in a JSON database.

---

## 🛠️ Technologies Used

- Python
- SHA-256
- JSON
- File System Operations
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
└── monitored_files/
    ├── test.txt
    └── important.txt
