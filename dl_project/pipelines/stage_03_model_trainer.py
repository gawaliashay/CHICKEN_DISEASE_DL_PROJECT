from dl_project.artifacts_mgr.artifact_generator import ConfigurationManager
from dl_project.components.model_trainer import ModelTrainer
from dl_project.base.logger import logger
from dl_project.base.exceptions import CustomException
from datetime import datetime
import sys




STAGE_NAME = "Model Training Pipeline"



class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):

        try:
            logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<")
            start_time = datetime.now()
            logger.info(f"Started {STAGE_NAME} at {start_time}")

            config = ConfigurationManager()
            training_config = config.get_training_config()
            training = ModelTrainer(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()

            logger.info(f">>>>>> Completed {STAGE_NAME} <<<<<<")
            end_time = datetime.now()
            logger.info(f"Completed {STAGE_NAME} at {end_time}")
            logger.info(f"Total time taken for {STAGE_NAME} is {end_time - start_time}")
        

        except Exception as e:
            logger.error(f">>>>>> Error occurred in {STAGE_NAME}: {e} <<<<<<")
            raise CustomException(e, sys)

