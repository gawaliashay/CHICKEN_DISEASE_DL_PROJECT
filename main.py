#main.py:

from datetime import datetime
from dl_project.base.logger import logger
from dl_project.pipelines.stage_01_data_ingestion import DataIngestionPipeline
from dl_project.pipelines.stage_02_prepare_base_model import PrepareBaseModelPipeline
from dl_project.pipelines.stage_03_model_trainer import ModelTrainingPipeline
from dl_project.pipelines.stage_04_model_evaluation import ModelEvaluationPipeline
from dl_project.base.exceptions import CustomException  # Import CustomException
import sys  # Import sys to pass it to CustomException
import os



os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Add at very top


STAGE_NAME = "Data Ingestion Stage"

try:
    start_time = datetime.now()
    logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<< at {start_time}")


    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()

    
    end_time = datetime.now()
    logger.info(f">>>>>> Completed {STAGE_NAME} <<<<<< at {end_time}")
    logger.info(f"Total time taken for {STAGE_NAME} is {end_time - start_time}")

except Exception as e:
    logger.error(f">>>>>> Error occurred in {STAGE_NAME}: {e} <<<<<<")
    raise CustomException(e, sys)  # Raise CustomException with the original exception


STAGE_NAME = "Prepare Base Model Stage"

try:
    start_time = datetime.now()
    logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<< at {start_time}")


    prepare_base_model_pipeline = PrepareBaseModelPipeline()
    prepare_base_model_pipeline.main()

    end_time = datetime.now()
    logger.info(f">>>>>> Completed {STAGE_NAME} <<<<<< at {end_time}")
    logger.info(f"Total time taken for {STAGE_NAME} is {end_time - start_time}")

except Exception as e:
    logger.error(f">>>>>> Error occurred in {STAGE_NAME}: {e} <<<<<<")
    raise CustomException(e, sys)


STAGE_NAME = "Model Training Stage"

try:
    start_time = datetime.now()
    logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<< at {start_time}")

    model_training_pipeline = ModelTrainingPipeline()
    model_training_pipeline.main()
    
    end_time = datetime.now()
    logger.info(f">>>>>> Completed {STAGE_NAME} <<<<<< at {end_time}")
    logger.info(f"Total time taken for {STAGE_NAME} is {end_time - start_time}")

except Exception as e:
    logger.error(f">>>>>> Error occurred in {STAGE_NAME}: {e} <<<<<<")
    raise CustomException(e, sys)


STAGE_NAME = "Model Evaluation Stage"

try:
    start_time = datetime.now()
    logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<< at {start_time}")

    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.main()

    end_time = datetime.now()
    logger.info(f">>>>>> Completed {STAGE_NAME} <<<<<< at {end_time}")
    logger.info(f"Total time taken for {STAGE_NAME} is {end_time - start_time}")

except Exception as e:
    logger.error(f">>>>>> Error occurred in {STAGE_NAME}: {e} <<<<<<")
    raise CustomException(e, sys)