import tensorflow as tf
from deepClassifier.entity import PrepareBaseModelConfig
from pathlib import Path
from deepClassifier import logger

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        try: 
            logger.info('Using VGG16 model')
            self.model = tf.keras.applications.vgg16.VGG16(
                input_shape = self.config.params_image_size,
                weights = self.config.params_weights,
                include_top = self.config.params_include_top             #Do not include last layer
            )

            base_model_path = self.config.base_model_path

            self.save_model(path = base_model_path, model = self.model)
            logger.info(f'Saving the VGG model in {base_model_path}')
        except Exception as e:
            raise e
        
    @staticmethod
    def _prepare_final_model(model, classes, freeze_all, freeze_till, learning_rate):
        try:
            if freeze_all:
                logger.info('Freezing all the layers')
                for layer in model.layers:
                    model.trainable = False 
            elif (freeze_till is not None) and (freeze_till>0):
                logger.info(f"Freezing till {freeze_till} layer")
                for layer in model.layers[:-freeze_till]:
                    model.trainable = False

            flatten_in = tf.keras.layers.Flatten()(model.output)
            prediction = tf.keras.layers.Dense(
                units = classes,
                activation = 'softmax'
            )(flatten_in)

            final_model = tf.keras.models.Model(
                inputs = model.input,
                outputs = prediction
            )

            final_model.compile(
                optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate),
                loss = tf.keras.losses.CategoricalCrossentropy(),
                metrics = ['accuracy']
            )
            final_model.summary()
            logger.info(f"Final Model created: {final_model.summary()}")
            return final_model
        except Exception as e:
            raise e
        
        
    def update_base_model(self):
        self.full_model = self._prepare_final_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)
        logger.info(f"Saving the updated model into {self.config.updated_base_model_path}")
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)