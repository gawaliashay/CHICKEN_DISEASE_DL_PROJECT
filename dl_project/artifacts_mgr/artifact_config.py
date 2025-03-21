#artifact_config.py

import os
from datetime import datetime
from dataclasses import dataclass
from pathlib import Path  # Import Path
from dl_project.constants.constants import *  # Ensure constants are defined

# Generate a timestamp to append to directories for uniqueness
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class DataIngestionConfig:
    artifacts_dir: Path = Path(os.path.join(ARTIFACTS_STORE))  # Use Path for type hint
    source_URL: str = "https://github.com/entbappy/Branching-tutorial/raw/master/Chicken-fecal-images.zip"
    zip_data_path: Path = Path(os.path.join(ARTIFACTS_STORE, "data_ingestion", TIMESTAMP, "zipped_data", "data.zip"))
    Local_data_path: Path = Path(os.path.join(ARTIFACTS_STORE, "data_ingestion", TIMESTAMP, "extracted_data"))
