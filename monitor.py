import os
import hashlib
import json
from datetime import datetime

MONITORED_FOLDER = "monitored_files"
DATABASE_FILE = "database.json"
LOG_FILE = "logs.txt"


def calculate_hash(file_path):
    """Calculate SHA-256 hash of a file."""

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


def load_database():
    """Load previously stored file hashes."""

    if not os.path.exists(DATABASE_FILE):
        return {}

    try:
        with open(DATABASE_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}


def save_database(database):
    """Save file hashes."""

    with open(DATABASE_FILE, "w") as file:
        json.dump(database, file, indent=4)


def write_log(message):
    """Write event to log file."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"[{timestamp}] {message}\n")


def scan_files():

    database = load_database()
    current_files = {}

    new_files = 0
    modified_files = 0
    deleted_files = 0
    unchanged_files = 0

    print("\nScanning files...\n")

    # Scan current files
    for root, directories, files in os.walk(MONITORED_FOLDER):

        for filename in files:

            file_path = os.path.join(root, filename)

            file_hash = calculate_hash(file_path)

            current_files[file_path] = file_hash

            # New file
            if file_path not in database:

                print(f"[NEW]       {file_path}")

                write_log(f"NEW FILE: {file_path}")

                new_files += 1

            # Modified file
            elif database[file_path] != file_hash:

                print(f"[MODIFIED]  {file_path}")

                write_log(f"MODIFIED: {file_path}")

                modified_files += 1

            # Unchanged file
            else:

                print(f"[OK]        {file_path}")

                unchanged_files += 1

    # Check deleted files
    for file_path in database:

        if file_path not in current_files:

            print(f"[DELETED]   {file_path}")

            write_log(f"DELETED: {file_path}")

            deleted_files += 1

    # Save new database
    save_database(current_files)

    # Summary
    total_files = len(current_files)

    print("\n========================================")
    print("           SCAN SUMMARY")
    print("========================================")

    print(f"Files currently scanned : {total_files}")
    print(f"New files               : {new_files}")
    print(f"Modified files          : {modified_files}")
    print(f"Deleted files           : {deleted_files}")
    print(f"Unchanged files         : {unchanged_files}")

    print("========================================")

    if modified_files > 0 or deleted_files > 0:

        print("STATUS: WARNING - CHANGES DETECTED!")

    elif new_files > 0:

        print("STATUS: NEW FILES DETECTED")

    else:

        print("STATUS: SECURE - NO CHANGES DETECTED")

    print("========================================\n")


def main():

    print("========================================")
    print("       FILE INTEGRITY MONITOR")
    print("========================================")

    print(f"Monitoring folder: {MONITORED_FOLDER}")

    scan_files()

if __name__ == "__main__":

    while True:

        print("\n========================================")
        print("       FILE INTEGRITY MONITOR")
        print("========================================")

        print("1. Scan files")
        print("2. View logs")
        print("3. View database")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            scan_files()

        elif choice == "2":

            if os.path.exists(LOG_FILE):

                with open(LOG_FILE, "r") as file:
                    print("\n========== ACTIVITY LOG ==========\n")
                    print(file.read())

            else:

                print("\nNo logs available.")

        elif choice == "3":

            if os.path.exists(DATABASE_FILE):

                with open(DATABASE_FILE, "r") as file:
                    print("\n========== FILE DATABASE ==========\n")
                    print(file.read())

            else:

                print("\nDatabase is empty.")

        elif choice == "4":

            print("\nExiting File Integrity Monitor...")
            break

        else:

            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")