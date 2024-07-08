import os
directory_path = 'S:\Ankamala\Files & Directories'

# Using os.listdir() 
entries = os.listdir(directory_path)
for entry in entries:
    print(entry)
