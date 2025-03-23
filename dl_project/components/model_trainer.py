import tensorflow as tf
from pathlib import Path
from dl_project.artifacts_mgr.artifact_entity import ModelTrainerArtifacts
from dl_project.base.logger import logger
from dl_project.base.exceptions import CustomException

class ModelTrainer:
    def __init__(self, config: ModelTrainerArtifacts):
        self.config = config

    def get_base_model(self):
        try:
            # Load the model
            self.model = tf.keras.models.load_model(
                self.config.updated_base_model_path
            )
            # Recompile the model
            self.model.compile(
                optimizer='adam',  # Use the same optimizer as before
                loss='categorical_crossentropy',  # Use the appropriate loss function
                metrics=['accuracy']  # Use the appropriate metrics
            )
        except Exception as e:
            logger.error(f"Error loading or compiling the base model: {e}")
            raise CustomException(f"Error loading or compiling the base model: {e}")

    def train_valid_generator(self):
        try:
            datagenerator_kwargs = dict(
                rescale=1.0 / 255,
                validation_split=0.20
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

            if self.config.params_is_augmentation:
                train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                    rotation_range=40,
                    horizontal_flip=True,
                    width_shift_range=0.2,
                    height_shift_range=0.2,
                    shear_range=0.2,
                    zoom_range=0.2,
                    **datagenerator_kwargs
                )
            else:
                train_datagenerator = valid_datagenerator

            self.train_generator = train_datagenerator.flow_from_directory(
                directory=self.config.training_data,
                subset="training",
                shuffle=True,
                **dataflow_kwargs
            )
        except Exception as e:
            logger.error(f"Error creating train/validation generators: {e}")
            raise CustomException(f"Error creating train/validation generators: {e}")

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        try:
            # Save the model in the native Keras format
            model.save(path)
        except Exception as e:
            logger.error(f"Error saving the model: {e}")
            raise CustomException(f"Error saving the model: {e}")

    def train(self):
        try:
            # Disable debug mode for now
            # tf.data.experimental.enable_debug_mode()

            self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
            self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

            self.model.fit(
                self.train_generator,
                epochs=self.config.params_epochs,
                steps_per_epoch=self.steps_per_epoch,
                validation_steps=self.validation_steps,
                validation_data=self.valid_generator
            )

            self.save_model(
                path=self.config.trained_model_path,
                model=self.model
            )
        except Exception as e:
            logger.error(f"Error during model training: {e}")
            raise CustomException(f"Error during model training: {e}")