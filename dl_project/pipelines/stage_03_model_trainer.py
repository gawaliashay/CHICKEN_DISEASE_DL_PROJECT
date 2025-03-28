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

            config = ConfigurationManager()
            training_config = config.get_training_artifacts()
            training = ModelTrainer(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()
        

        except Exception as e:
            logger.error(f">>>>>> Error occurred in {STAGE_NAME}: {e} <<<<<<")
            raise CustomException(e, sys)

