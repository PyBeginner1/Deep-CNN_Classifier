from deepClassifier import logger
from deepClassifier.config import ConfigurationManager
from deepClassifier.components import PrepareCallbacks, Training

STAGE_NAME = 'Training'

def main():
    config = ConfigurationManager()
    prepare_callbacks_model_config = config.get_prepare_callback_config()
    prepare_callbacks_model = PrepareCallbacks(config=prepare_callbacks_model_config)
    callback_list = prepare_callbacks_model.get_tb_ckpt_callbacks()

    training_config = config.get_training_config()
    training_model = Training(config=training_config)
    training_model.get_base_model()
    training_model.train_valid_generator()
    training_model.train(
        callback_list = callback_list
    )


if __name__ == "__main__":
    try:
        logger.info(f"\n{'-'*75}")
        logger.info(f"\n\n>>>>>> {STAGE_NAME} stage started <<<<<<")
        main()
        logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        