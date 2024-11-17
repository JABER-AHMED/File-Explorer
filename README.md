File System Explorer Documentation
This program is a simple and interactive file system explorer that allows you to scan a directory, group files by their types, and display metadata for each file. It uses Python's pathlib, humanize, and datetime modules to make the output readable and user-friendly.

Features
Directory Validation: Ensures the provided path is a valid directory.

File Grouping: Groups files by their extensions (e.g., .txt, .py) or marks them as "No Extension" if missing.

Readable Metadata: Displays human-friendly file metadata:
File name
File size (e.g., 4.2 KB, 3.1 MB)
Creation time (e.g., 3 days ago)
Last modification time (e.g., 5 minutes ago)

Interactive User Prompt: Asks the user for a directory to scan.

Dependencies
The humanize library: Install with: pip install humanize

Usage Instructions
Run the Script: Execute the script by running:
python file_explorer.py
Enter Directory Path: Provide a valid directory path when prompted.

View Results: The program will:

Validate the directory.
Group files by type.
Display file metadata in a tabular format.
Example Output

File System Explorer
---------------------
Enter the directory path to scan: C:\Users\YourName\Documents

🔍 Scanning C:\Users\YourName\Documents...

=== *.txt Files (3) ===
Name                           Size       Created                        Last Modified
-----------------------------------------------------------------------------------------------
example1.txt                   4.3 KB     3 days ago                    2 hours ago
notes.txt                      1.2 KB     2 weeks ago                   1 week ago
todo.txt                       900 B      1 month ago                   3 days ago
-----------------------------------------------------------------------------------------------

=== Files with No Extension (1) ===
Name                           Size       Created                        Last Modified
-----------------------------------------------------------------------------------------------
README                         500 B      5 months ago                  4 months ago
-----------------------------------------------------------------------------------------------

Code Components
1. FileManager Class
Handles file-related operations:

validate_directory(directory): Validates if the provided directory path exists.
extract_metadata(file_path): Extracts and formats file metadata.
group_files_by_type(directory): Groups files in the directory by their extensions.

2. FileDisplay Class
Formats and displays grouped files in a readable table format.

3. main() Function
Provides a user interface.
Validates user input and orchestrates file grouping and display.