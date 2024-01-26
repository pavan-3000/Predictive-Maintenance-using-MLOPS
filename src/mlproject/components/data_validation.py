from src.mlproject.logger import logging
from src.mlproject.exception import CustomException

from src.mlproject.config.configuration import ConfigManger
from src.mlproject.entity.config_entity import DataValidationConfig

import sys
import os
import pandas as pd


class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config
        
    def validate_all_columns(self) -> bool:
        try:
            validation_status = True
            
            data = pd.read_csv(self.config.unzip_data_dir)
            all_col = list(data.columns)
            
            all_schema = self.config.all_schema.keys()
            
            for col in all_col:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f'validation_staus : {validation_status}')
                else:
                    validation_status =True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"validation status: {validation_status}")
                        
                
            
            
            
        except Exception as e:
            raise CustomException(e,sys)
        