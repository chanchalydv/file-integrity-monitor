# 🔐 File Integrity Monitor

A beginner-friendly cybersecurity project that monitors files for unauthorized changes using SHA-256 hashing.

## 📌 About the Project

The File Integrity Monitor (FIM) scans files inside a monitored directory and creates a unique SHA-256 hash for each file.

During later scans, the new hash is compared with the previously stored hash.

If the hash changes, the program detects that the file has been modified.

The system can detect:

- New files
- Modified files
- Deleted files
- Unchanged files

It also maintains an activity log and stores file hashes in a JSON database.

## 🛠️ Technologies Used

- Python
- SHA-256
- JSON
- File System Operations
- Python `hashlib`
- Python `os`
- Python `datetime`

## 📂 Project Structure

```text
file-integrity-monitor/
│
├── monitor.py
├── database.json
├── logs.txt
├── README.md
│
└── monitored_files/
    ├── test.txt
    └── important.txt
```

## ⚙️ How It Works

The File Integrity Monitor works in the following steps:

1. The program scans the `monitored_files` directory.
2. It finds all files inside the directory.
3. A SHA-256 hash is calculated for each file.
4. The hash is stored in `database.json`.
5. During the next scan, a new hash is calculated.
6. The new hash is compared with the previously stored hash.
7. If the hashes are different, the file has been modified.
8. If a previously stored file no longer exists, it is marked as deleted.
9. Important events are recorded in `logs.txt`.

### 🔐 Hash Comparison

```text
File
  ↓
SHA-256 Hash
  ↓
database.json
  ↓
Scan Again
  ↓
New SHA-256 Hash
  ↓
Compare Hashes
  ↓
Hash Same → File Unchanged
Hash Different → File Modified
```

## 🔍 Features

### 1. New File Detection

Detects newly added files.

Example:

```text
[NEW] monitored_files\test.txt
```

### 2. Modified File Detection

Detects when an existing file has been changed.

Example:

```text
[MODIFIED] monitored_files\test.txt
```

### 3. Deleted File Detection

Detects when a previously monitored file has been deleted.

Example:

```text
[DELETED] monitored_files\test.txt
```

### 4. Unchanged File Detection

Confirms that a file has not changed.

Example:

```text
[OK] monitored_files\test.txt
```

### 5. SHA-256 Hashing

Creates a digital fingerprint for each monitored file.

### 6. Activity Logging

Detected events are stored in:

```text
logs.txt
```

### 7. Hash Database

File hashes are stored in:

```text
database.json
```

### 8. Command-Line Menu

The program provides:

```text
1. Scan files
2. View logs
3. View database
4. Exit
```

## ▶️ How to Run

### Step 1 — Open the Project

Open the `file-integrity-monitor` folder in VS Code.

### Step 2 — Open the Terminal

Make sure the terminal is inside the project folder.

### Step 3 — Run the Program

```bash
python monitor.py
```

### Step 4 — Select an Option

The program will display:

```text
========================================
       FILE INTEGRITY MONITOR
========================================

1. Scan files
2. View logs
3. View database
4. Exit

Enter your choice:
```

## 🧪 Testing

The project was tested using different file-change scenarios.

| Test | Expected Result |
|---|---|
| Create a new file | New file detected |
| Run scan without changing file | File remains unchanged |
| Modify a file | Modification detected |
| Delete a file | Deletion detected |
| View logs | Activity displayed |
| View database | SHA-256 hashes displayed |

## 📊 Example Output

```text
========================================
       FILE INTEGRITY MONITOR
========================================

1. Scan files
2. View logs
3. View database
4. Exit

Enter your choice: 1

Scanning files...

[OK]        monitored_files\test.txt
[OK]        monitored_files\important.txt

========================================
           SCAN SUMMARY
========================================

Files currently scanned : 2
New files               : 0
Modified files          : 0
Deleted files           : 0
Unchanged files         : 2

STATUS: SECURE - NO CHANGES DETECTED
========================================
```

## 🎓 Learning Outcomes

Through this project, I learned:

- Python file handling
- SHA-256 hashing
- Hash comparison
- JSON data storage
- File system operations
- Logging
- Basic cybersecurity concepts
- Command-line application development

## 🚀 Future Improvements

Possible future improvements include:

- Real-time file monitoring
- Email alerts
- Desktop notifications
- Web-based dashboard
- User authentication
- Exportable security reports
- Graphical user interface

## ⚠️ Disclaimer

This project is created for educational and cybersecurity learning purposes.

It should only be used on files and systems that you own or have permission to monitor.