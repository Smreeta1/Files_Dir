from datetime import datetime, timezone
from os import scandir

def convert_date(timestamp):
    d = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    formatted_date = d.strftime('%d %b %Y')
    return formatted_date

def get_files(dir_path):
    dir_entries = scandir(dir_path)
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')


dir_path = r'S:\Ankamala\Files & Directories'
get_files(dir_path)
