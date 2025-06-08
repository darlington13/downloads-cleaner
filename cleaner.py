import os
import time
from pathlib import Path
import shutil

# addition of ordering  desktop as well 
DOWNLOADS_PATH = Path.home() / "Downloads"
DESKTOP_PATH =Path.home()/ "Desktop"
DAYS_OLD = 30  
file_types  = ['.zip', '.exe', '.msi', '.pdf']  

def file_is_old(file_path, days=DAYS_OLD):
    file_age = time.time() - os.path.getmtime(file_path)
    return file_age > days * 86400  

def clean_downloads():
    print(f"Cleaning Downloads folder: {DOWNLOADS_PATH}")
    deleted_files = 0

    for file in DOWNLOADS_PATH.iterdir():
        if file.is_file():
            if file.suffix in file_types and file_is_old(file):
                print(f"Deleting: {file.name}")
                try:
                    file.unlink()
                    deleted_files += 1
                except Exception as e:
                    print(f"Error deleting {file}: {e}")

    print(f"Deleted {deleted_files} files.")

def order_desktop():
    print(f"Cleaning desktop: {DESKTOP_PATH}")
    ordered_files = 0
    
    # addition of grouping files in folders on the desktop
    pdf_folder = DESKTOP_PATH / "PDFs"
    
    for file in DESKTOP_PATH.iterdir():
        
        if file.is_file() and file.suffix == '.pdf':
            print("Creating/using PDF folder")
            try:
                
                pdf_folder.mkdir(exist_ok=True)
                
                shutil.move(str(file), str(pdf_folder / file.name))
                ordered_files += 1
            except Exception as e:
                print(f"Error moving file {file}: {e}")
    
    print(f"Ordered {ordered_files} files")




if __name__ == "__main__":
    clean_downloads()
    order_desktop()
