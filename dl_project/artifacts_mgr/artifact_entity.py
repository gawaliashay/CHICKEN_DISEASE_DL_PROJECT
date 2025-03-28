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


@dataclass(frozen=True)
class ModelTrainerArtifacts:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list

@dataclass(frozen=True)
class ModelEvaluationArtifacts:
    path_of_model: Path
    training_data: Path
    mlflow_uri: str
    all_params: dict
    params_image_size: list
    params_batch_size: int