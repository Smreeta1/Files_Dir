import os

for dirpath, dirnames, files in os.walk( "."):  # traversal begins from the directory specified ('.' for the current directory)
    print(f"Found directory: {dirpath}")
    for file_name in files:
        print(file_name)
