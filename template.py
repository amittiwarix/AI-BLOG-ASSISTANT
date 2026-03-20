import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')  

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py"
]

for file in list_of_files:
    file_path = Path(file)
    fildir,filename = os.path.split(file)
    if fildir!="":
        os.makedirs(fildir, exist_ok=True)
        logging.info(f"Directory; {fildir} for the file: {filename}")
    if (not os.path.exists(file)) or (os.path.getsize(file) == 0):
        with open(file, 'w') as f:
            pass
        logging.info(f"created empty file: {file}")
    else:
        logging.info(f"file: {file} already exists")


    