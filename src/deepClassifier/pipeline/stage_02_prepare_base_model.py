from deepClassifier import logger
from deepClassifier.config import ConfigurationManager
from deepClassifier.components import PrepareBaseModel

STAGE_NAME = 'Prepare Base Model'

def main():
    config = ConfigurationManager()
    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
    prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()



if __name__ == "__main__":
    try:
        logger.info(f"\n\n>>>>>> {STAGE_NAME} stage started <<<<<<")
        main()
        logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
