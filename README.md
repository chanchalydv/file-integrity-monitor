# 🔐 File Integrity Monitor

A beginner-friendly cybersecurity project built with Python that detects unauthorized changes to files using SHA-256 hashing.

## 📌 About the Project

The File Integrity Monitor (FIM) is a cybersecurity tool that checks files inside a monitored directory and detects whether they have been changed, created, or deleted.

The program creates a unique SHA-256 hash for each monitored file. During the next scan, it calculates the hash again and compares it with the previously stored hash.

If the hash changes, it indicates that the file content has been modified.

The system can detect:

- 🆕 New files
- ✏️ Modified files
- 🗑️ Deleted files
- ✅ Unchanged files

The project also maintains an activity log and stores file hashes in a JSON database.

---

## 🎯 Project Objective

The main objective of this project is to understand the basic concept of **File Integrity Monitoring (FIM)** in cybersecurity.

This project demonstrates how cryptographic hashing can be used to detect unauthorized modifications to important files.

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
```

---

## ⚙️ How It Works

The File Integrity Monitor follows these basic steps:

```text
              File
                ↓
          SHA-256 Hash
                ↓
        Store Hash in Database
                ↓
          Scan File Again
                ↓
        Calculate New Hash
                ↓
          Compare Hashes
                ↓
        Detect File Status
```

### 🔐 SHA-256 Hashing

SHA-256 generates a unique hash value based on the contents of a file.

For example:

```text
File Content
     ↓
SHA-256
     ↓
Unique Hash
```

If the contents of the file change, the SHA-256 hash will also change.

Therefore:

```text
Old Hash = New Hash
       ↓
✅ File Unchanged
```

and

```text
Old Hash ≠ New Hash
       ↓
⚠️ File Modified
```

---

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/chanchalydv/file-integrity-monitor.git
```

### Step 2: Open the Project Folder

```bash
cd file-integrity-monitor
```

### Step 3: Run the Program

```bash
python monitor.py
```

The program will scan the files inside the `monitored_files` directory and compare their current hashes with the previously stored hashes.

---

## 🧪 How to Test the Project

You can test the File Integrity Monitor by modifying one of the monitored files.

### Test Modified File

1. Open:

```text
monitored_files/test.txt
```

2. Change the content of the file.
3. Save the file.
4. Run the program again:

```bash
python monitor.py
```

The program should detect the file as:

```text
Modified
```

because the SHA-256 hash has changed.

### Test New File

Create a new file inside:

```text
monitored_files/
```

Then run:

```bash
python monitor.py
```

The program should detect:

```text
New File
```

### Test Deleted File

Delete a monitored file and run the program again.

The program should detect:

```text
Deleted File
```

### Test Unchanged File

If a file has not been changed since the previous scan, the program should detect:

```text
Unchanged
```

---

## 🔍 Detection Types

| Status | Description |
|---|---|
| 🆕 New | A new file has been detected |
| ✏️ Modified | The file content has changed |
| 🗑️ Deleted | A previously monitored file has been deleted |
| ✅ Unchanged | The file has not changed |

---

## 📝 Logs

The project records file activity in:

```text
logs.txt
```

The log can contain information about detected file changes and scan activity.

---

## 💾 Database

The project stores file hashes in:

```text
database.json
```

The stored hashes are used during future scans to determine whether a file has changed.

---

## 📸 Project Screenshot

A screenshot of the project is available inside the:

```text
screenshots/
```

folder.

---

## 🔐 Cybersecurity Concept

File Integrity Monitoring is an important cybersecurity concept used to detect unauthorized changes to files.

It can help identify unexpected modifications to important files and can be useful for security monitoring.

This project provides a basic implementation of the concept using:

- File system operations
- SHA-256 hashing
- Hash comparison
- JSON storage
- Activity logging

---

## 🚀 Future Improvements

The project can be improved by adding:

- 🔄 Real-time file monitoring
- 📧 Email notifications
- 🚨 Security alerts
- 🌐 Web-based dashboard
- 📁 Multiple monitored directories
- 🔑 User authentication
- 📊 Monitoring statistics
- ⚡ Automated continuous monitoring

---

## 📚 Learning Outcomes

Through this project, I learned:

- Basics of File Integrity Monitoring
- How SHA-256 hashing works
- How to calculate file hashes using Python
- File and directory handling
- Working with JSON files
- Maintaining activity logs
- Detecting file modifications
- Basic cybersecurity monitoring concepts

---

## 👩‍💻 Author

**Chanchal Yadav**

B.Tech CSE – Cyber Security

---

## ⭐ Project

This project was created as a beginner cybersecurity project to understand **File Integrity Monitoring, SHA-256 hashing, file system operations, and basic security concepts**.

If you find this project useful, feel free to ⭐ the repository.
