import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import (DataIngestionConfig)



from cnnClassifier import logger
from kaggle.api.kaggle_api_extended import KaggleApi

import os


class DataIngestion:

    def __init__(self, config):
        self.config = config

    def download_file(self):

        os.makedirs(
            self.config.root_dir,
            exist_ok=True
        )

        logger.info("Downloading dataset from Kaggle")

        api = KaggleApi()
        api.authenticate()

        api.dataset_download_files(
            self.config.dataset_name,
            path=self.config.unzip_dir,
            unzip=True
        )

        logger.info("Dataset downloaded successfully")

        
        
    

    