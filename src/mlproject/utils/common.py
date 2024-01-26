import os
import yaml
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import json
import joblib
from pathlib import Path 
from typing import Any  

from src.mlproject.logger import logging
import sys
from src.mlproject.exception import CustomException


from box import ConfigBox
from ensure import ensure_annotations


@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info("loaded yaml sucessfully")
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e,sys)
    
    
@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
        logging.info("json is created")
    

@ensure_annotations
def create_directory(path_dir:list,verbose=True):
    for path in path_dir:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logging.info(f"created directory at {path}")
