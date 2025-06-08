import os
import time
from pathlib import Path
import shutil

# Customize these variables
DOWNLOADS_PATH = Path.home() / "Downloads"
DAYS_OLD = 30  # Files older than this will be deleted
FILE_TYPES_TO_DELETE = ['.zip', '.exe', '.msi']  

def file_is_old(file_path, days=DAYS_OLD):
    file_age = time.time() - os.path.getmtime(file_path)
    return file_age > days * 86400  # 86400 seconds in a day

def clean_downloads():
    print(f"Cleaning Downloads folder: {DOWNLOADS_PATH}")
    deleted_files = 0

    for file in DOWNLOADS_PATH.iterdir():
        if file.is_file():
            if file.suffix in FILE_TYPES_TO_DELETE and file_is_old(file):
                print(f"Deleting: {file.name}")
                try:
                    file.unlink()
                    deleted_files += 1
                except Exception as e:
                    print(f"Error deleting {file}: {e}")

    print(f"Deleted {deleted_files} files.")

if __name__ == "__main__":
    clean_downloads()
