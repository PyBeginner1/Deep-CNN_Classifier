from deepClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from deepClassifier.utils.common import *
from deepClassifier.entity import DataIngestionConfig, PrepareBaseModelConfig



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
            
            return prepare_base_model_config
        except Exception as e:
            raise e