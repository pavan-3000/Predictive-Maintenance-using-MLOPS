from src.mlproject.logger import logging
from src.mlproject.exception import CustomException

from src.mlproject.pipeline.data_ingestion_pipeline import IngestionPipeline

import sys


try:
    logging.info("runnnnnnnnn")
    
    obj = IngestionPipeline()
    obj.main()
    
    
    logging.info("level 1 is completed susscessfully")
except Exception as e:
    raise CustomException(e,sys)