from deepClassifier.config import ConfigurationManager
from deepClassifier.components import DataIngestionComponent
from deepClassifier import logger


STAGE_NAME = 'Data Ingestion'


def main():
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestionComponent(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()



if __name__ =='__main__':
    try:
        logger.info(f"\n\n>>>>>> {STAGE_NAME} stage started <<<<<<")
        main() 
        logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e