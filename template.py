import os
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

# variable called project

project_name= "cnnClassifier"

#created the list of the files that will be created

#1) .github/workflows/.gitkeep : useful when implementing CI/CD, we gonna create main.yaml under workflows
#   but intitially we are not creating later we will create, since github dont allow empty folders we are create a dummy file
#   called .gitkeep

#2) src folder as source folder where project folder to keep project files
#    src/{project_name}/__init__.py , here __init__.py acts as a constructor to make this folder as a package 
#    later to be used to import
#3) components folder for data ingestion, data validation etc, inside components again __init__.py 
#    constructor to make it local package
#before implementing modular coding we first experiment in jupyter notebook, thats why we created 
#research folder with trials.ipynb

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html'
]

# In windows os for file paths backward slash is used, but in mac forward slash, 
# in order for the above folder creation to work in windows with out throwing path not found error,
# we are importing path class and writing the following code:
for filepath in list_of_files:
    filepath= Path(filepath)
    filedir,filename =os.path.split(filepath)

    if filedir !='':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory;{filedir} for the file:{filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f'creating empty file: {filepath}')

    else:
        logging.info(f'{filename} already exists')

## after executing this template.py file folder and files will be created
## commit the changes to git, with following commands
#""" 1. git add .
 #   2. git commit -m
 #   3. git push origin main"""


     


