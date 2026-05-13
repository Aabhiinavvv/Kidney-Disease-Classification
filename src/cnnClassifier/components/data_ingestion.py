import os
import subprocess
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
import urllib.request as request
from cnnClassifier.entity.config_entity import (DataIngestionConfig)



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {os.path.getsize(self.config.local_data_file)}")
        
        
    

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory.
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        for root, _, files in os.walk(unzip_path):
            for file in files:
                if file.lower().endswith(".rar"):
                    rar_path = os.path.join(root, file)
                    logger.info(f"Extracting nested archive {rar_path} into {unzip_path}")
                    subprocess.run(
                        ["tar", "-xf", rar_path, "-C", unzip_path],
                        check=True
                    )
