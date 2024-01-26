from src.mlproject.logger import logging
from src.mlproject.exception import CustomException

from src.mlproject.config.configuration import ConfigManger
from src.mlproject.entity.config_entity import DataValidationConfig
from src.mlproject.components.data_validation import DataValidation

import sys


class validationPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        try:
            logging.info('stating dat validation')
            cofig = ConfigManger()
            config_v = cofig.get_data_validation_config()
            data_validation = DataValidation(config=config_v)
            data_validation.validate_all_columns()
            logging.info('validaetion completed')
            
            
        except Exception as e:
            raise CustomException(e,sys)