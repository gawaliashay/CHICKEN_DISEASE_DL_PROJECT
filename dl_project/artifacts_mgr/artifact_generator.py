#artifact_generator.py

import os
from dl_project.constants.constants import *
from dl_project.base.logger import logger
from dl_project.base.exceptions import CustomException  # Import CustomException
from dl_project.utils.utils import create_directories, read_yaml
from dl_project.artifacts_mgr.artifact_config import (DataIngestionConfig, 
                                                      PrepareBaseModelConfig,
                                                      ModelTrainerConfig,
                                                      ModelEvaluationConfig)
from dl_project.artifacts_mgr.artifact_entity import (DataIngestionArtifacts,
                                                       PrepareBaseModelArtifacts,
                                                       ModelTrainerArtifacts,
                                                       ModelEvaluationArtifacts)
import sys  # Import sys to pass it to CustomException


class ConfigurationManager:
    def __init__(self, data_ingestion_config=DataIngestionConfig, 
                 data_ingestion_artifacts=DataIngestionArtifacts, 
                 prepare_base_model_config=PrepareBaseModelConfig, 
                 prepare_base_model_artifacts=PrepareBaseModelArtifacts,
                 model_trainer_config=ModelTrainerConfig,
                 model_trainer_artifacts=ModelTrainerArtifacts,
                 model_evaluation_config=ModelEvaluationConfig,
                 model_evaluation_artifacts=ModelEvaluationArtifacts):
        
        self.data_ingestion_config = data_ingestion_config
        self.data_ingestion_artifacts = data_ingestion_artifacts
        self.prepare_base_model_config = prepare_base_model_config
        self.prepare_base_model_artifacts = prepare_base_model_artifacts
        self.model_trainer_config = model_trainer_config
        self.model_trainer_artifacts = model_trainer_artifacts
        self.model_evaluation_config = model_evaluation_config
        self.model_evaluation_artifacts = model_evaluation_artifacts


        self.config = ARTIFACT_CONFIG_FILE_PATH
        self.params =  read_yaml(PARAMS_FILE_PATH)

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
            create_directories([config.root_dir])
            logger.info(f"Created data_ingestion directory at {config.root_dir}")

            # Create DataIngestionArtifacts object
            data_ingestion_artifacts = DataIngestionArtifacts(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                zip_data_path=config.zip_data_path,
                local_data_path=config.Local_data_path
            )

            logger.info("Data ingestion artifacts configured successfully")
            return data_ingestion_artifacts

        except Exception as e:
            logger.error(f"Error occurred while configuring data ingestion artifacts: {e}")
            raise CustomException(e, sys)  # Raise CustomException with the original exception
        
    
    def get_prepare_base_model_artifacts(self) -> PrepareBaseModelArtifacts:
        try:
            config = self.prepare_base_model_config

            # Create the root directory for base model artifacts
            create_directories([config.root_dir])
            logger.info(f"Created prepare_base_model directory at {config.root_dir}")

            # Validate that all required parameters are present
            required_params = ['IMAGE_SIZE', 'LEARNING_RATE', 'INCLUDE_TOP', 'WEIGHTS', 'CLASSES']
            for param in required_params:
                if not hasattr(self.params, param):
                    raise ValueError(f"Missing required parameter '{param}' in params.yaml.")

            # Log parameter values for debugging
            logger.info(f"Using parameters: IMAGE_SIZE={self.params.IMAGE_SIZE}, "
                        f"LEARNING_RATE={self.params.LEARNING_RATE}, "
                        f"INCLUDE_TOP={self.params.INCLUDE_TOP}, "
                        f"WEIGHTS={self.params.WEIGHTS}, "
                        f"CLASSES={self.params.CLASSES}")

            # Create PrepareBaseModelArtifacts object
            prepare_base_model_artifacts = PrepareBaseModelArtifacts(
                root_dir=config.root_dir,
                base_model_path=config.base_model_path,
                updated_base_model_path=config.updated_base_model_path,
                params_image_size=self.params.IMAGE_SIZE,  # Access using dot notation
                params_learning_rate=self.params.LEARNING_RATE,  # Access using dot notation
                params_include_top=self.params.INCLUDE_TOP,  # Access using dot notation
                params_weights=self.params.WEIGHTS,  # Access using dot notation
                params_classes=self.params.CLASSES  # Access using dot notation
            )

            logger.info("Base model artifacts configured successfully")
            return prepare_base_model_artifacts

        except Exception as e:
            logger.error(f"Error occurred while preparing base model artifacts: {e}")
            raise CustomException(e, sys)  # Raise CustomException with the original exception
        

    def get_training_artifacts(self) -> ModelTrainerArtifacts:

        try:
            config = self.model_trainer_config
            params = self.params
            training_data = os.path.join(self.data_ingestion_config.Local_data_path, "Chicken-fecal-images")
            create_directories([
                Path(config.root_dir)
            ])

            model_trainer_artifacts = ModelTrainerArtifacts(
                root_dir=Path(config.root_dir),
                trained_model_path=Path(config.trained_model_path),
                updated_base_model_path=Path(self.prepare_base_model_config.updated_base_model_path),
                training_data=Path(training_data),
                params_epochs=params["EPOCHS"],
                params_batch_size=params["BATCH_SIZE"],
                params_is_augmentation=params["AUGMENTATION"],
                params_image_size=params["IMAGE_SIZE"]
            )

            return model_trainer_artifacts 

        except Exception as e:  
            logger.error(f"Error occurred while preparing model training artifacts: {e}")
            raise CustomException(e, sys)  
        
    def get_evaluation_artifacts(self) -> ModelEvaluationArtifacts:

        try: 
            config = self.model_evaluation_config
            create_directories([Path(config.root_dir)])

            training_data = os.path.join(self.data_ingestion_config.Local_data_path, "Chicken-fecal-images")

            eval_config = ModelEvaluationArtifacts(
            path_of_model=self.prepare_base_model_config.updated_base_model_path,
            training_data=training_data,
            mlflow_uri=MLFLOW_URI,
            all_params=self.params,
            params_image_size=self.params["IMAGE_SIZE"],
            params_batch_size=self.params["BATCH_SIZE"]
            )
            return eval_config
        
        except Exception as e:
            logger.error(f"Error occurred while preparing model evaluation artifacts: {e}") 
            raise CustomException(e, sys)