from pathlib import Path
from collections import defaultdict
from datetime import datetime
import humanize


class FileManager:
    @staticmethod
    def directory_validation(directory):
        path = Path(directory)
        if not path.is_dir():
            raise ValueError(f"{directory} is not a valid directory.")
        return path

    @staticmethod
    def metadata_extraction(file_path):
        stat = file_path.stat()
        return {
            'Name': file_path.name,
            'Size (KB)': humanize.naturalsize(stat.st_size),
            'Created': humanize.naturaltime(datetime.fromtimestamp(stat.st_ctime)),
            'Last Modified': humanize.naturaltime(datetime.fromtimestamp(stat.st_mtime)),
        }

    @staticmethod
    def group_files_by_type(directory):
        grouped_files = defaultdict(list)
        for file in directory.iterdir():
            if file.is_file():
                extension = file.suffix.lower() if file.suffix else 'No Extension'
                grouped_files[extension].append(file)
        return grouped_files


class FileDisplay:
    @staticmethod
    def display_grouped_files(grouped_files):
        for extension, files in grouped_files.items():
            header = f"=== *.{extension} Files ({len(files)}) ===" if extension != 'No Extension' else f"=== Files with No Extension ({len(files)}) ==="
            print(f"\n{header}")
            print(f"{'Name':<30} {'Size (KB)':<10} {'Created':<30} {'Last Modified'}")
            print("-" * 95)
            for file in files:
                metadata = FileManager.metadata_extraction(file)
                print(f"{metadata['Name']:<30} {metadata['Size (KB)']:<10} {metadata['Created']:<30} {metadata['Last Modified']}")
            print("-" * 95)


def main():
    print("File Explorer")
    print("---------------------")
    directory = input("Enter the directory path to scan: ").strip()
    
    try:
        validated_dir = FileManager.directory_validation(directory)
        print(f"\n Scanning {validated_dir}...")

        grouped_files = FileManager.group_files_by_type(validated_dir)
        
        if not grouped_files:
            print("No files found in the directory.")
            return
        
        FileDisplay.display_grouped_files(grouped_files)
    
    except ValueError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Permission Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
