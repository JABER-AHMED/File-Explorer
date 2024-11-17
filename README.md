# File Explorer Documentation

This program is a simple and interactive file system explorer that allows you to scan a directory, group files by their types, and display metadata for each file. It uses Python's `pathlib`, `humanize`, and `datetime` modules to make the output readable and user-friendly.

---

## Features
- **Directory Validation**: Ensures the provided path is a valid directory.
- **File Grouping**: Groups files by their extensions (e.g., `.txt`, `.py`) or marks them as "No Extension" if missing.
- **Readable Metadata**: Displays human-friendly file metadata:
  - File name
  - File size (e.g., `4.2 KB`, `3.1 MB`)
  - Creation time (e.g., `3 days ago`)
  - Last modification time (e.g., `5 minutes ago`)
- **Interactive User Prompt**: Asks the user for a directory to scan.

---

## Dependencies
- **The `humanize` library**: Install it using:
  ```bash
  pip install humanize

# Usage Instructions

## Run the Script
Execute the script by running:

```bash
python file_explorer.py

## Enter Directory Path
Provide a valid directory path when prompted.

---

## View Results
The program will:

- **Validate the directory.**
- **Group files by type.**
- **Display file metadata in a tabular format.**

## Expected Output

![image](https://github.com/user-attachments/assets/401ff998-fff5-4154-8cd0-4014af49216e)
