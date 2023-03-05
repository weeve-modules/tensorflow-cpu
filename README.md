# TensorFlow CPU

|           |                                                                                     |
| --------- | ----------------------------------------------------------------------------------- |
| Name      | tensorflow-cpu                                                                      |
| Version   | v1.0.0                                                                              |
| DockerHub | [weevenetwork/tensorflow-cpu](https://hub.docker.com/r/weevenetwork/tensorflow-cpu) |
| Authors   | Jakub Grzelak                                                                       |

- [TensorFlow CPU](#tensorflow-cpu)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

Use your pre-trained TensorFlow (Keras or non Keras) model with weeve modules. This module supports only CPU models and we plan to make a separate module to run TensorFlow with CUDA. The model should be available to the module via a downloadable URL (zipped model folder) or it should be stored in the edge device local filesystem (unzipped or regular folder). The module will take input data and then compose a tensor with data in the order assigned to the Ordered Labels environment variable. Later, the module will input that tensor into the model.

If the model is Keras, then the module uses high-level API to load the model. Otherwise, the module uses low-level API (SavedModel).

The module uses a function provided in Prediction Function config (env FORWARD_PROP_FUNCTION) to make a prediction. For instance, if Prediction Function is `predict` then the module uses `model.predict(X)` to make a prediction, if Prediction function is `__call__` then `model(X)`, etc.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                   | Environment Variables  | type   | Description                                                                                                                                                 |
| ---------------------- | ---------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Model ZIP Download URL | MODEL_ZIP_DOWNLOAD_URL | string | If model is stored online, then provide a download URL to parse the model in a zip file. Leave empty field to search for the model in the local filesystem. |
| Model Folderpath       | MODEL_LOCAL_FOLDERPATH | string | If model is stored in the local filesystem (above field for URL was left empty), then provide a path to the folder containing the model.                    |
| Keras                  | IS_KERAS               | string | Whether the model is Keras or not.                                                                                                                          |
| Prediction Function    | FORWARD_PROP_FUNCTION  | string | Name of the prediction (forward propagation function), i.e. `predict` or `__call__`                                                                         |
| Input Labels           | INPUT_LABELS           | string | Input data labels in the order of feeding into the model. Later a TensorFlow tensor will be created to feed that data into the model in the given order.    |
| Output Label           | OUTPUT_LABEL           | string | The output label at which data is dispatched.                                                                                                               |

### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output) |
| EGRESS_URLS           | string | HTTP ReST endpoints for the next module        |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
requests
tensorflow-cpu
```

## Input

Input to this module is:

-   JSON body single object, example:

```json
{
    "temperature": 12,
    "volume": 1.3,
    "pressure": 0.32
}
```

-   array of JSON body objects, example:

```json
[
    {
        "temperature": 12,
        "volume": 1.3,
        "pressure": 0.32
    },
    {
        "temperature": 13,
        "volume": 2.1,
        "pressure": 0.34
    }
]
```

## Output

Output of this module is

-   JSON body single object, example:

```json
{
    "prediction": 14.323
}
```

-   array of JSON body objects, example:

```json
[
    {
        "prediction": 14.323
    },
    {
        "prediction": 13.45
    }
]
```
