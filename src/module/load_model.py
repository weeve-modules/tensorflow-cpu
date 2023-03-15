import tensorflow as tf
from logging import getLogger
from api import setup_logging
from .params import PARAMS

setup_logging()
log = getLogger("load_model")


def load_model():
    # flag whether use downloaded model or locally stored model (for locally stored, MODEL_LOCAL_FOLDERPATH env should be volume bind to container ./local_model)
    model_folder_name = (
        PARAMS["EXTRACTED_MODEL_PATH"]
        if PARAMS["MODEL_ZIP_DOWNLOAD_URL"]
        else PARAMS["MODEL_LOCAL_FOLDERPATH"]
    )

    try:
        if PARAMS["IS_KERAS"]:
            # high-level API loading: https://www.tensorflow.org/guide/keras/save_and_serialize?hl=en
            log.info(f"Loading Keras model: {model_folder_name} ...")
            model = tf.keras.models.load_model(model_folder_name)
            log.info("Successfully loaded Keras model ...")

        else:
            # low-level API loading: https://www.tensorflow.org/guide/saved_model?hl=en
            log.info(f"Loading the model: {model_folder_name} ...")
            model = tf.saved_model.load(model_folder_name)
            log.info("Successfully loaded the model ...")

        return model

    except Exception as e:
        log.error(f"Exception when loading the model: {e}")
        return None
