import os
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
                with open('tf_model.zip', 'wb') as model_file:
                    model_file.write(resp.content)
                log.info("Successfully downloaded the model.")

                # un-zip the model
                log.info("Unzipping the model ...")
                file_list_before_unzipping = os.listdir()
                with zipfile.ZipFile('tf_model.zip', 'r') as zip_ref:
                    zip_ref.extractall()
                    extracted_folders = [x for x in os.listdir() if x not in file_list_before_unzipping]
                    if len(extracted_folders) > 0:
                        PARAMS["EXTRACTED_MODEL_PATH"] = extracted_folders[0]
                    else:
                        log.error("Could not extract the model from zipped file. Probably empty archive.")

                log.info("Successfully unzipped the model.")

            else:
                log.error(f"Could not download the model. {resp.status_code} - {resp.reason}")

        except Exception as e:
            log.error(f"Exception when downloading the model: {e}")
