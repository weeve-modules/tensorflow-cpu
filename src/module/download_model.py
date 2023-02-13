import requests
import zipfile
from logging import getLogger
from api import setup_logging
from .params import PARAMS

setup_logging()
log = getLogger("download_model")

def download_model():
    if PARAMS["MODEL_ZIP_DOWNLOAD_URL"]:
        try:
            # download the model from the given url
            log.info(f"Downloading model from: {PARAMS['MODEL_ZIP_DOWNLOAD_URL']} ...")
            resp = requests.get(PARAMS["MODEL_ZIP_DOWNLOAD_URL"], allow_redirects=True)

            # save the model
            if resp.status_code == 200:
                log.info(f"Saving the zip model inside Docker container ...")
                with open(PARAMS["DOWNLOADED_MODEL_ZIP_FILENAME"], 'wb') as model_file:
                    model_file.write(resp.content)
                log.info("Successfully downloaded the model.")

                # un-zip the model
                log.info("Unzipping the model ...")
                with zipfile.ZipFile(PARAMS["DOWNLOADED_MODEL_ZIP_FILENAME"], 'r') as zip_ref:
                    zip_ref.extractall()
                log.info("Successfully unzipped the model.")

            else:
                log.error(f"Could not download the model. {resp.status_code} - {resp.reason}")

        except Exception as e:
            log.error(f"Exception when downloading the model: {e}")
