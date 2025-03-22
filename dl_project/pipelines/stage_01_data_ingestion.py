#stage_01_data_ingestion.py

from dl_project.artifacts_mgr.artifact_generator import ConfigurationManager
from dl_project.components.data_ingestion import DataIngestion
from dl_project.artifacts_mgr.artifact_entity import DataIngestionArtifacts
from dl_project.artifacts_mgr.artifact_config import DataIngestionConfig
from dl_project.base.logger import logger
from dl_project.base.exceptions import CustomException
from datetime import datetime
import sys  # Import sys to pass it to CustomException


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        self.config = ConfigurationManager(DataIngestionConfig, DataIngestionArtifacts)
        self.data_ingestion_artifacts = self.config.get_data_ingestion_artifacts()
        self.data_ingestion = DataIngestion(self.data_ingestion_artifacts)

    def main(self):
        
        try:
            # Perform data ingestion steps
            self.data_ingestion.download_file()
            self.data_ingestion.extract_zip_file()

        except Exception as e:
            # Log the error and raise a CustomException
            logger.error(f"Error occurred during {STAGE_NAME}: {e}")
            raise CustomException(e, sys)