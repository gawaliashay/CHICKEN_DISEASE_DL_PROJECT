#artifact_generator.py

import os
from dl_project.constants.constants import *
from dl_project.base.logger import logger
from dl_project.base.exceptions import CustomException  # Import CustomException
from dl_project.utils.utils import create_directories
from dl_project.artifacts_mgr.artifact_config import DataIngestionConfig
from dl_project.artifacts_mgr.artifact_entity import DataIngestionArtifacts
import sys  # Import sys to pass it to CustomException


class ConfiguartionManager:
    def __init__(self, data_ingestion_config=DataIngestionConfig, data_ingestion_artifacts=DataIngestionArtifacts):
        self.data_ingestion_config = data_ingestion_config
        self.data_ingestion_artifacts = data_ingestion_artifacts

        self.config = ARTIFACT_CONFIG_FILE_PATH
        self.params = PARAMS_FILE_PATH

        try:
            # Create necessary directories
            create_directories([ARTIFACTS_STORE])
            logger.info(f"Created artifacts store directory at {ARTIFACTS_STORE}")
        except Exception as e:
            logger.error(f"Error occurred while creating artifacts store directory: {e}")
            raise CustomException(e, sys)  # Raise CustomException with the original exception

    def get_data_ingestion_artifacts(self) -> DataIngestionArtifacts:
        try:
            config = self.data_ingestion_config

            # Create directories for data ingestion artifacts
            create_directories([self.data_ingestion_config.artifacts_dir])
            logger.info(f"Created artifacts directory at {self.data_ingestion_config.artifacts_dir}")

            # Create DataIngestionArtifacts object
            data_ingestion_artifacts = DataIngestionArtifacts(
                artifacts_dir=self.data_ingestion_config.artifacts_dir,
                source_URL=self.data_ingestion_config.source_URL,
                zip_data_path=self.data_ingestion_config.zip_data_path,
                local_data_path=self.data_ingestion_config.Local_data_path
            )

            logger.info("Data ingestion artifacts configured successfully")
            return data_ingestion_artifacts

        except Exception as e:
            logger.error(f"Error occurred while configuring data ingestion artifacts: {e}")
            raise CustomException(e, sys)  # Raise CustomException with the original exception