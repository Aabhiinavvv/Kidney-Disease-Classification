import os
from pathlib import Path
import logging

#logging string

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",

    # Main package
    f"src/{project_name}/__init__.py",

    # Submodules
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/utils/__init__.py",

    # Config files
    "config/config.yaml",
    "params.yaml",
    "dvc.yaml",

    # Other root files
    "main.py",
    "requirements.txt",
    "setup.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir , exist_ok=True)
        logging.info(f"Creating Directory {filedir} for the file : {filename}")

        
