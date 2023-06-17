import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "Classifications"

list_of_files = [
    
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]

for file_path in list_of_files:
    
    filepath = Path(file_path)                         # to convert Linux path into WindowsPath
    filedir = filepath.parent
    filename = filepath.name

    if filedir!="":
        try :
            os.makedirs(filedir,exist_ok=True)
            logging.info("Creating directory: {} for file: {} ".format(filedir,filename))
        
        except Exception as e:
            print(e,"Error while creating the directory. Directory already exists")
        
    
    if  not filepath.exists():
        with open (filepath,"w") as f:
            logging.info("Creating the file : {}".format(filename))
            pass

    else:
        logging.info("File already exists")
