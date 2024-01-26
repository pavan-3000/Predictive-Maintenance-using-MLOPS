from src.mlproject.logger import logging
from src.mlproject.exception import CustomException

from src.mlproject.pipeline.data_validation_pipeline import validationPipeline


import sys

"""
try:
    logging.info("runnnnnnnnn")
    
    obj = IngestionPipeline()
    obj.main()
    
    
    logging.info("level 1 is completed susscessfully")
except Exception as e:
    raise CustomException(e,sys)
"""


try:
    logging.info('stared level 2 data valsidaeton')
    obj = validationPipeline()
    obj.main()
except Exception as e:
    raise CustomException(e,sys)