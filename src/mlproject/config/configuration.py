from src.mlproject.logger import logging
from src.mlproject.exception import CustomException

from src.mlproject.constants import *
from src.mlproject.utils.common import read_yaml,create_directory
from src.mlproject.entity.config_entity import DataIngestionConfig
from src.mlproject.entity.config_entity import DataValidationConfig
import sys

class ConfigManger:
    def __init__(
        self,
        config_path = CONFIG_FILE_PATH,
        params_path = PARAMS_FILE_PATH,
        schema_path = SCHEMA_FILE_PATH):
        
        self.config =  read_yaml(config_path)
        self.schema = read_yaml(schema_path)
        self.params = read_yaml(params_path)
        
        create_directory([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            
            config = self.config.data_ingestion
            
            create_directory([config.root_dir])
            
            data_ingesion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir
            )
            return data_ingesion_config
        
        
        
        except Exception as e:
            raise CustomException(e,sys)
        

    def get_data_validation_config(self) -> DataValidationConfig:
        config  = self.config.data_validation
        schema = self.schema.COLUMNS
        
        
        try:
            create_directory(config.root_dir)
            data_validation_config = DataValidationConfig(
                root_dir=config.root_dir,
                unzip_data_dir=config.unzip_data_dir,
                STATUS_FILE= config.STATUS_FILE,
                all_schema=schema
            )
            
            return data_validation_config
            
            
            
            
            
        except Exception as e:
            raise CustomException(e,sys)
            
        