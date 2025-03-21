#artifact_entity.py

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionArtifacts:
    artifacts_dir: Path
    source_URL: str
    zip_data_path: Path
    local_data_path: Path