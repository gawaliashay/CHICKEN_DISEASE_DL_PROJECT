#artifact_entity.py

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionArtifacts:
    root_dir: Path
    source_URL: str
    zip_data_path: Path
    local_data_path: Path


@dataclass(frozen=True)
class PrepareBaseModelArtifacts:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int