import sys
from dl_project.artifacts_mgr.artifact_generator import ConfigurationManager
from dl_project.components.prepare_base_model import PrepareBaseModel
from dl_project.base.logger import logger
from dl_project.base.exceptions import CustomException


STAGE_NAME = "Prepare Base Model Stage"

class PrepareBaseModelPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
        self.prepare_base_model_artifacts = self.config.get_prepare_base_model_artifacts()
        self.prepare_base_model = PrepareBaseModel(self.prepare_base_model_artifacts)

    def main(self):
        try:
            # Get the base model
            self.prepare_base_model.get_base_model()
            self.prepare_base_model.update_base_model()

        except Exception as e:
            # Log the error and raise a CustomException
            logger.error(f"Error occurred during {STAGE_NAME}: {e}")
            raise CustomException(e, sys)