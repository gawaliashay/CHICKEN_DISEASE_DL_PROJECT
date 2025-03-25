#model_evaluation.py

import tensorflow as tf
from pathlib import Path
from dl_project.artifacts_mgr.artifact_entity import ModelEvaluationArtifacts
from dl_project.utils.utils import save_json
import mlflow
import mlflow.keras
from urllib.parse import urlparse
import numpy as np
import sys
from urllib.parse import quote
import os
from dl_project.base.logger import logger
from dl_project.base.exceptions import CustomException
from dl_project.constants.constants import MLFLOW_URI


class Evaluation:
    def __init__(self, config: ModelEvaluationArtifacts):
        self.config = config

    
    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)

    
    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    

    def log_into_mlflow(self):
        try:
            # Use local file storage
            mlflow_uri = MLFLOW_URI
            
            # Set the experiment name
            experiment_name = "Chicken_Disease_VGG16Model"
            if not mlflow.get_experiment_by_name(experiment_name):
                mlflow.create_experiment(experiment_name)
            mlflow.set_experiment(experiment_name)
            
            # Start MLflow run
            with mlflow.start_run():
                # Log parameters
                mlflow.log_params(self.config.all_params)
                
                # Log metrics
                mlflow.log_metrics({
                    "loss": self.score[0], 
                    "accuracy": self.score[1]
                })
                
                # Get input example for signature
                input_example = next(self.valid_generator)[0][0]  # Get first batch, first sample
                
                
                # Log the model - updated syntax
                mlflow.keras.log_model(
                    model=self.model,  # Changed from keras_model to model
                    artifact_path="model",
                    registered_model_name="VGG16Model"
                )

                
                
                logger.info("Successfully logged model to MLflow")
                
        except Exception as e:
            logger.error(f"Failed to log to MLflow: {str(e)}")
            raise CustomException(e, sys)