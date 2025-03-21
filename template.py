#template.py 
# This script creates the project structure for the machine learning project.



import os
from pathlib import Path

# The project structure is created with the following files and directories:
project_name = "dl_project"

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/data_connector/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/constants/constants.py",
    f"{project_name}/artifacts_mgr/__init__.py",
    f"{project_name}/artifacts_mgr/artifact_config.yaml",
    f"{project_name}/artifacts_mgr/artifact_entities.py",
    f"{project_name}/artifacts_mgr/artifact_generator.py",
    f"{project_name}/pipelines/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/utils.py",
    f"{project_name}/base/__init__.py",
    f"{project_name}/base/logger.py",
    f"{project_name}/base/exceptions.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "main.py",
    "pyproject.toml",
    "config/params.yaml",
    "README.md",
    ".env",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"File already exists: {filepath}")