from deepClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from deepClassifier.utils.common import *
from deepClassifier.entity import DataIngestionConfig


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