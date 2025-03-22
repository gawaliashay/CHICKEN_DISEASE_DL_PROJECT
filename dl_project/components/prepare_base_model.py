import os
import sys
import tensorflow as tf
from pathlib import Path
from dl_project.artifacts_mgr.artifact_entity import PrepareBaseModelArtifacts
from dl_project.base.logger import logger
from dl_project.base.exceptions import CustomException


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelArtifacts):
        self.config = config

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        """Save the model to the specified path."""
        try:
            model.save(path)
            logger.info(f"Model saved successfully at {path}")
        except Exception as e:
            logger.error(f"Error occurred while saving the model to {path}: {e}")
            raise CustomException(e, sys)

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        """Load a saved model from the given path."""
        try:
            model = tf.keras.models.load_model(path)
            logger.info(f"Model loaded successfully from {path}")
            return model
        except Exception as e:
            logger.error(f"Error occurred while loading the model from {path}: {e}")
            raise CustomException(e, sys)

    def get_base_model(self):
        """Fetch the base model (VGG16) with the specified configuration."""
        try:
            self.model = tf.keras.applications.vgg16.VGG16(
                input_shape=self.config.params_image_size,
                weights=self.config.params_weights,
                include_top=self.config.params_include_top
            )
            self.save_model(path=self.config.base_model_path, model=self.model)
        except Exception as e:
            logger.error(f"Error occurred while fetching the base model: {e}")
            raise CustomException(e, sys)

    def _prepare_full_model(self, model, classes, freeze_all, freeze_till, learning_rate):
        """Prepare the full model by adding custom layers on top of the base model."""
        try:
            if freeze_all:
                for layer in model.layers:
                    model.trainable = False
            elif (freeze_till is not None) and (freeze_till > 0):
                for layer in model.layers[:-freeze_till]:
                    model.trainable = False

            flatten_in = tf.keras.layers.Flatten()(model.output)
            prediction = tf.keras.layers.Dense(
                units=classes,
                activation="softmax"
            )(flatten_in)

            full_model = tf.keras.models.Model(
                inputs=model.input,
                outputs=prediction
            )

            full_model.compile(
                optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
                loss=tf.keras.losses.CategoricalCrossentropy(),
                metrics=["accuracy"]
            )

            full_model.summary()
            return full_model

        except Exception as e:
            logger.error(f"Error occurred while preparing the full model: {e}")
            raise CustomException(e, sys)

    def update_base_model(self):
        """Update the base model by adding custom layers and saving the updated model."""
        try:
            if not os.path.exists(self.config.updated_base_model_path):
                # Load the base model
                self.model = self.load_model(path=self.config.base_model_path)

                # Prepare the full model
                self.full_model = self._prepare_full_model(
                    model=self.model,
                    classes=self.config.params_classes,
                    freeze_all=True,
                    freeze_till=None,
                    learning_rate=self.config.params_learning_rate
                )

                # Save the updated model
                self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

        except Exception as e:
            logger.error(f"Error occurred while updating the base model: {e}")
            raise CustomException(e, sys)