from deepClassifier.config import ConfigurationManager
from deepClassifier.components import Evaluation
from deepClassifier import logger

STAGE_NAME = 'Evaluation'

def main():
    config = ConfigurationManager()
    eval_config = config.get_evaluation_config()
    evaluation = Evaluation(config = eval_config)
    evaluation.evaluation()
    evaluation.save_score()

if __name__ == "__main__":
    try:
        logger.info(f"\n{'-'*75}")
        logger.info(f"\n\n>>>>>> {STAGE_NAME} stage started <<<<<<")
        main()
        logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

