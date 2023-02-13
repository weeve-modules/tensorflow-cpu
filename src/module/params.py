from os import getenv

PARAMS = {
    "MODEL_ZIP_DOWNLOAD_URL": getenv("MODEL_ZIP_DOWNLOAD_URL"),
    "DOWNLOADED_MODEL_ZIP_FILENAME": getenv("DOWNLOADED_MODEL_ZIP_FILENAME") if getenv("DOWNLOADED_MODEL_ZIP_FILENAME").strip().split(".")[-1] == "zip" else getenv("DOWNLOADED_MODEL_ZIP_FILENAME") + ".zip",
    "MODEL_LOCAL_FOLDERPATH": getenv("MODEL_LOCAL_FOLDERPATH"),
    "WITH_KERAS": True if getenv("WITH_KERAS", "False") == "True" else False,
    "FORWARD_PROP_FUNCTION": getenv("FORWARD_PROP_FUNCTION", "__call__"),
    "ORDERED_LABELS": [label.strip() for label in getenv("ORDERED_LABELS", "").split(',')],
    "OUTPUT_LABEL": getenv("OUTPUT_LABEL", "prediction")
}
