from dl_project.artifacts_mgr.artifact_generator import ConfigurationManager
from dl_project.components.model_evaluation import Evaluation
from dl_project.base.logger import logger
from dl_project.base.exceptions import CustomException
from datetime import datetime
import sys


STAGE_NAME = "Model Evaluation Pipeline"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):

        try:

            config = ConfigurationManager()
            evaluation_config = config.get_evaluation_artifacts()
            evaluation = Evaluation(config=evaluation_config)
            evaluation.evaluation()
            evaluation.save_score()
            evaluation.log_into_mlflow()

        except Exception as e:
            logger.error(f">>>>>> Error occurred in {STAGE_NAME}: {e} <<<<<<")
            raise CustomException(e, sys)