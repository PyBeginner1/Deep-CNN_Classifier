from deepClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from deepClassifier.utils.common import *
from deepClassifier.entity import (DataIngestionConfig, PrepareBaseModelConfig, 
                                   PrepareCallbacksConfig, TrainingConfig, EvaluationConfig)
import os
from deepClassifier import logger

class ConfigurationManager:
    def __init__(self, 
                config_file_path = CONFIG_FILE_PATH, 
                params_file_path = PARAMS_FILE_PATH):
        try:
            self.config = read_yaml(config_file_path)
            self.params = read_yaml(params_file_path)
            create_directories([self.config.artifacts_root])
        except Exception as e:
            raise e

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            config = self.config.data_ingestion            

            root_dir = config.root_dir
            
            create_directories([config.root_dir])

            source_URL = config.source_URL
            local_data_file = config.local_data_file
            unzip_dir = config.unzip_dir

            
            data_ingestion_config = DataIngestionConfig(
                root_dir= root_dir,
                source_URL= source_URL,
                local_data_file= local_data_file,
                unzip_dir= unzip_dir
            )
            logger.info(f"Data Ingestion config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise e


    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        try:
            config = self.config.prepare_base_model
            params = self.params

            root_dir = config.root_dir
            create_directories([root_dir])
            base_model_path = config.base_model_path
            updated_base_model_path = config.updated_base_model_path

            params_image_size = params.IMAGE_SIZE
            params_learning_rate = params.LEARNING_RATE
            params_include_top = params.INCLUDE_TOP
            params_weights = params.WEIGHTS
            params_classes = params.CLASSES

            prepare_base_model_config = PrepareBaseModelConfig(
                root_dir=Path(root_dir),
                base_model_path=Path(base_model_path),
                updated_base_model_path=Path(updated_base_model_path),
                params_image_size=params_image_size,
                params_learning_rate=params_learning_rate,
                params_include_top=params_include_top,
                params_weights=params_weights,
                params_classes=params_classes
            )
            
            logger.info(f"Prepare Base Model config: {prepare_base_model_config}")
            return prepare_base_model_config
        except Exception as e:
            raise e
        
    def get_prepare_callback_config(self) -> PrepareCallbacksConfig:
        try:
            config = self.config.prepare_callbacks

            root_dir = config.root_dir
            model_checkpoint_dir = os.path.dirname(config.checkpoint_model_filepath)   

            create_directories([
                Path(model_checkpoint_dir),
                Path(config.tensorboard_root_log_dir)
            ])         

            prepare_callback_config = PrepareCallbacksConfig(
                root_dir=Path(root_dir),
                tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
                checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
            )
            
            logger.info(f"Prepare Callback config: {prepare_callback_config}")
            return prepare_callback_config
        except Exception as e:
            raise e
        

    def get_training_config(self) -> TrainingConfig:
        try:
            training = self.config.training
            prepare_base_model = self.config.prepare_base_model
            data_ingestion = self.config.data_ingestion
            params=self.params

            create_directories([Path(training.root_dir)])

            training_config = TrainingConfig(
                root_dir = Path(training.root_dir),
                trained_model_path=Path(training.trained_model_path),
                updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
                training_data=Path(os.path.join(data_ingestion.unzip_dir,"PetImages")),
                params_epoch=params.EPOCHS,
                params_batch_size=params.BATCH_SIZE,
                params_image_size=params.IMAGE_SIZE,
                params_is_augmentation=params.AUGMENTATION
            )
            logger.info(f"Training config: {training_config}")
            return training_config
        except Exception as e:
            raise e


    def get_evaluation_config(self) -> EvaluationConfig:
        try:
            eval_config = EvaluationConfig(
                path_of_model=self.config.training.trained_model_path,
                training_data= self.config.data_ingestion.unzip_dir,
                params_image_size=self.params.IMAGE_SIZE,
                params_batch_size = self.params.BATCH_SIZE
            )
            logger.info(f"Evaluation config: {eval_config}")
            return eval_config
        except Exception as e:
            raise e