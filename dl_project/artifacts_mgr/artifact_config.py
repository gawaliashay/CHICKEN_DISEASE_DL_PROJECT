#artifact_config.py

import os
from datetime import datetime
from dataclasses import dataclass
from pathlib import Path  # Import Path
from dl_project.constants.constants import *  # Ensure constants are defined
from dl_project.utils.utils import read_yaml

# Generate a timestamp to append to directories for uniqueness
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

# Define the artifacts directory
artifacts_dir: Path = Path(os.path.join(ARTIFACTS_STORE))

@dataclass
class DataIngestionConfig:
      # Use Path for type hint
    root_dir: Path = Path(os.path.join(artifacts_dir, "data_ingestion"))
    source_URL: str = "https://github.com/entbappy/Branching-tutorial/raw/master/Chicken-fecal-images.zip"
    zip_data_path: Path = Path(os.path.join(root_dir, "zipped_data", ))
    Local_data_path: Path = Path(os.path.join(root_dir, "extracted_data"))

@dataclass
class PrepareBaseModelConfig:
    root_dir: Path = Path(os.path.join(artifacts_dir, "prepare_base_model"))
    base_model_path: Path = Path(os.path.join(root_dir/BASE_MODEL_FILE))
    updated_base_model_path: Path = Path(os.path.join(root_dir/UPDATED_BASE_MODEL_FILE))

@dataclass
class ModelTrainerConfig:
    root_dir: Path = Path(os.path.join(artifacts_dir, "trained_model"))
    trained_model_path: Path = Path(os.path.join(root_dir, TRAINED_MODEL_FILE))
    training_data: Path = Path(os.path.join(root_dir, "training_data"))

@dataclass
class ModelEvaluationConfig:
    root_dir: Path = Path(os.path.join(artifacts_dir, "evaluate_model"))
    path_of_model: Path = Path(os.path.join(root_dir, TRAINED_MODEL_FILE))
    training_data: Path = Path(os.path.join(root_dir, "training_data"))
    mlflow_uri: str = MLFLOW_URI
    #all_params: dict = read_yaml(PARAMS_FILE_PATH)

