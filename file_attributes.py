import os

directory_path = 'S:\Ankamala\Files & Directories'


with os.scandir(directory_path) as dir_contents:
    for entry in dir_contents:
        info = entry.stat()
        print(f"{entry.name}: {info.st_mtime}")
