from src.mlproject.logger import logging
from src.mlproject.exception import CustomException

from src.mlproject.config.configuration import ConfigManger
from src.mlproject.entity.config_entity import DataIngestionConfig

import sys
import os
import gdown
import zipfile
class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
    
    def Download_zip(self):
        try:
            
            source = self.config.source_URL
            save_path = self.config.local_data_file
            os.makedirs("artifacts/data-ingestion",exist_ok=True)
            
            
            file_id  = source.split('/')[-2]
            prefix = 'https://drive.google.com/uc?export=download&id='
            gdown.download(prefix+file_id,save_path)
            logging.info("zip downloaded suscessfully")
            
            
            
            
            
        except Exception as e:
            raise CustomException(e,sys) 
        
        
        
    def extract_zip(self):
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path,exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file,'r') as f:
                f.extractall(unzip_path)
            
            
        except Exception as e:
            raise CustomException(e,sys)
            