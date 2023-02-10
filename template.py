import os
from pathlib import Path
import logging 


logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s')


package_name = 'deepClassifier'


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",               #Testing a Function
    "tests/integration/__init__.py",        #Checking if components in Pipeline are working accordingly
    "configs/config.yaml",                  #Configuration
    "dvc.yaml",                             #To create Data Version Control Pipeline
    "params.yaml",                          #Contains our training parameters
    "init_setup.sh",                        #Shell script file which will help in setting up environment
    "requirements.txt",
    "requirements_dev.txt",                 #Only for developers
    "setup.py",
    "setup.cfg",                            #Create python packages
    "pyproject.toml",                       #Create python packages
    "tox.ini",                              #Testing a file locally
    "research/trails.ipynb"                 #For testing
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    #Create directory
    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Directore created: {filedir} for file name: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass                            #Creates an empty folder
            logging.info(f'Created empty file: {filepath}')
    else:
        logging.info(f"{filename} already exists")