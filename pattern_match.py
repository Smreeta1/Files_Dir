import os

# Directory path
directory_path = 'dummy files'

# Iterate through files in the directory
for f_name in os.listdir(directory_path):
    if f_name.startswith('dummy_') :
        print(f_name)
    elif f_name.endswith('.txt'):
        print(f_name)
    else:
        print("Pattern does not match ")
