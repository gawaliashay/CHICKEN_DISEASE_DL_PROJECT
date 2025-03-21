#main.py:

from datetime import datetime
from dl_project.base.logger import logger
from dl_project.pipelines.stage_01_data_ingestion import DataIngestionPipeline
from dl_project.base.exceptions import CustomException  # Import CustomException
import sys  # Import sys to pass it to CustomException


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<")
    start_time = datetime.now()
    logger.info(f"Started {STAGE_NAME} at {start_time}")


    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()

    
    logger.info(f">>>>>> Completed {STAGE_NAME} <<<<<<")
    end_time = datetime.now()
    logger.info(f"Completed {STAGE_NAME} at {end_time}")
    logger.info(f"Total time taken for {STAGE_NAME} is {end_time - start_time}")

except Exception as e:
    logger.error(f">>>>>> Error occurred in {STAGE_NAME}: {e} <<<<<<")
    raise CustomException(e, sys)  # Raise CustomException with the original exception