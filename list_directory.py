import os
directory_path = 'S:\Ankamala\Files & Directories'

# Using os.scandir() 
with os.scandir(directory_path) as entries:
    for entry in entries:
        print(entry.name)

