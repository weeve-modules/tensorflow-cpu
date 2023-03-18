"""
This file implements module's main logic.
Data processing should happen here.

Edit this file to implement your module.
"""

import tensorflow as tf
import numpy as np
from logging import getLogger
from .load_model import load_model
from .params import PARAMS

log = getLogger("module")

try:
    FORWARD_PROP_FUNCTION = getattr(load_model(), PARAMS["FORWARD_PROP_FUNCTION"])
except AttributeError:
    log.error(
        f"Error. TensorFlow model does not have an attribute {PARAMS['FORWARD_PROP_FUNCTION']}. Check provided forward propagation function name."
    )
    exit(1)


def module_main(received_data: any) -> [any, str]:
    """
    Process received data by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        any: Processed data that are ready to be sent to the next module or None if error occurs.
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Processing ...")

    try:
        with tf.device("cpu"):
            if type(received_data) == list:
                X = np.array(
                    [
                        [data[label] for label in PARAMS["INPUT_LABELS"]]
                        for data in received_data
                    ]
                )
                y_hat = FORWARD_PROP_FUNCTION(X).data.tolist()
                processed_data = [{PARAMS["OUTPUT_LABEL"]: y[0]} for y in y_hat]
            else:
                X = np.array(
                    [received_data[label] for label in PARAMS["INPUT_LABELS"]]
                ).reshape(1, -1)
                processed_data = {
                    PARAMS["OUTPUT_LABEL"]: FORWARD_PROP_FUNCTION(X).item()
                }

        return processed_data, None

    except Exception as e:
        return None, f"Exception in the module business logic: {e}"
