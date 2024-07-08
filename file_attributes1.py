#using pathlib
from pathlib import Path
current_dir = Path('S:\Ankamala\Files & Directories')
for path in current_dir.iterdir():
    info = path.stat()
    print(info.st_mtime)