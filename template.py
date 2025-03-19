#template.py 
# This script creates the project structure for the machine learning project.



import os
from pathlib import Path

# The project structure is created with the following files and directories:
project_name = "mlProject"

list_of_files = [

    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",  
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/components/model_deployment.py",
    f"src/{project_name}/data_connector/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/constants/constants.py",
    f"src/{project_name}/artifacts_mgr/__init__.py",
    f"src/{project_name}/artifacts_mgr/artifact_paths.py",
    f"src/{project_name}/artifacts_mgr/artifact_entities.py",
    f"src/{project_name}/artifacts_mgr/artifact_generation.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/utils.py",
    f"src/{project_name}/base/__init__.py",
    f"src/{project_name}/base/logger.py",
    f"src/{project_name}/base/exceptions.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "main.py",
    "setup.py",
    "pyproject.toml",
    "config/hyperparameters.yaml",
    "config/data_schema.yaml",
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