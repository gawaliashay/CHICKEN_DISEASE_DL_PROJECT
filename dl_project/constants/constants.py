#constants.py:

from pathlib import Path

SOURCE_URL = "https://github.com/entbappy/Branching-tutorial/raw/master/Chicken-fecal-images.zip"

ARTIFACT_CONFIG_FILE_PATH = Path("dl_project/artifacts_mgr/artifact_config.py")
ARTIFACTS_STORE = Path("artifacts_store")
PARAMS_FILE_PATH = Path("config/params.yaml")


ZIPPED_DATA_FILE: str = "data.zip"

BASE_MODEL_FILE: str = "base_model.keras"
UPDATED_BASE_MODEL_FILE: str = "base_model_updated.keras"

TRAINED_MODEL_FILE: str = "model.keras"