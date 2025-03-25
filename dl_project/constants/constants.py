#constants.py:

from pathlib import Path
import os
from urllib.parse import quote

SOURCE_URL = "https://github.com/entbappy/Branching-tutorial/raw/master/Chicken-fecal-images.zip"

ARTIFACT_CONFIG_FILE_PATH = Path("dl_project/artifacts_mgr/artifact_config.py")
ARTIFACTS_STORE = Path("artifacts_store")
PARAMS_FILE_PATH = Path("config/params.yaml")


ZIPPED_DATA_FILE: str = "data.zip"

BASE_MODEL_FILE: str = "base_model.h5"
UPDATED_BASE_MODEL_FILE: str = "base_model_updated.h5"

TRAINED_MODEL_FILE: str = "model.h5"

MLRUNS_DIR = Path("f{ARTIFACTS_STORE}/mlruns").absolute()
MLFLOW_URI = os.getenv("MLFLOW_TRACKING_URI", f"file:///{quote(str(MLRUNS_DIR))}")