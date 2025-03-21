#data_ingestion.py

import os
import sys
import urllib.request as request
import zipfile
from dl_project.base.logger import logger
from dl_project.base.exceptions import CustomException
from dl_project.constants.constants import *
from dl_project.utils.utils import get_size
from dl_project.utils.utils import create_directories
from pathlib import Path
from dl_project.artifacts_mgr.artifact_entity import DataIngestionArtifacts
from dl_project.artifacts_mgr.artifact_config import DataIngestionConfig
from urllib.error import URLError, HTTPError  # For specific URL-related exceptions


class DataIngestion:
    def __init__(self, data_ingestion_artifacts: DataIngestionArtifacts):
        self.data_ingestion_artifacts = data_ingestion_artifacts

    def download_file(self):
        logger.info("***Downloading the file***")

        try:
            # Ensure the directory exists using create_directories
            zip_data_path = Path(self.data_ingestion_artifacts.zip_data_path)
            create_directories([zip_data_path.parent])  # Create parent directories

            if not os.path.exists(zip_data_path):
                logger.info(f"Downloading the data from {self.data_ingestion_artifacts.source_URL}")
                filename, headers = request.urlretrieve(
                    url=self.data_ingestion_artifacts.source_URL,
                    filename=zip_data_path
                )
                logger.info(f"{filename} downloaded! with following info: \n{headers}")
            else:
                logger.info(f"File already exists at {zip_data_path}")
                logger.info(f"Size of the file: {get_size(zip_data_path)}")
        except (URLError, HTTPError) as e:
            logger.error(f"URL error occurred while downloading the file: {e}")
            raise CustomException(e, sys)
        except Exception as e:
            logger.error(f"Error occurred while downloading the file: {e}")
            raise CustomException(e, sys)

    def extract_zip_file(self):
        logger.info("***Extracting the file***")

        try:
            local_data_path = Path(self.data_ingestion_artifacts.local_data_path)
            zip_data_path = Path(self.data_ingestion_artifacts.zip_data_path)

            if not os.path.exists(local_data_path):
                with zipfile.ZipFile(zip_data_path, 'r') as zip_ref:
                    zip_ref.extractall(local_data_path)  # Extract to the local_data_path
                logger.info(f"Data extracted at {local_data_path}")
            else:
                logger.info(f"Extracted data already present at {local_data_path}")
        except zipfile.BadZipFile as e:
            logger.error(f"Error occurred while extracting the zip file: {e}")
            raise CustomException(e, sys)
        except Exception as e:
            logger.error(f"Unexpected error occurred while extracting the file: {e}")
            raise CustomException(e, sys)