from src.mlproject.logger import logging
from src.mlproject.exception import CustomException

from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.config.configuration import DataIngestionConfigManager

import sys


class IngestionPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        try:
            logging.info('initial data ingestion')
            cofig = DataIngestionConfigManager()
            config_ingestion =cofig.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=config_ingestion)
            data_ingestion.Download_zip()
            data_ingestion.extract_zip()
            logging.info('data injestion is compoleted completed')
        except Exception as e:
            raise CustomException(e,sys)