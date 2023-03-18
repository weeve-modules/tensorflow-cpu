from os import getenv

PARAMS = {
    "MODEL_ZIP_DOWNLOAD_URL": getenv("MODEL_ZIP_DOWNLOAD_URL"),
    "MODEL_LOCAL_FOLDERPATH": getenv("MODEL_LOCAL_FOLDERPATH"),
    "IS_KERAS": True if getenv("IS_KERAS", "False") == "True" else False,
    "FORWARD_PROP_FUNCTION": getenv("FORWARD_PROP_FUNCTION", "__call__"),
    "INPUT_LABELS": [label.strip() for label in getenv("INPUT_LABELS", "").split(",")],
    "OUTPUT_LABEL": getenv("OUTPUT_LABEL", "prediction"),
}
