import os 
import sys
import numpy as np
import pandas as pd

'''Defining all the constants related to training pipeline'''

TARGET_COLUMN="Result"
PIPELINE_NAME="NetworkSecurity"
ARTIFACT_DIR="artifacts"
FILE_NAME:str="phisingData.csv"
TEST_FILE_NAME:str="test.csv"
TRAIN_FILE_NAME:str="train.csv"

SCHEMA_FILE_PATH=os.path.join("data_schema","schema.yaml")

'''Data Ingeestion related constants start with DATA_INGESTION_VAR_NAME'''

DATA_INGESTION_COLLECTION_NAME:str="Network_Data"
DATA_INGESTION_DATABASE_NAME:str="Rohit"
DATA_INGESTION_FILE_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float=0.2

'''Data Validation related constants start with DATA_VALIDATION_VAR_NAME'''

DATA_VALIDATION_DIR_NAME:str="data_validation"
DATA_VALIDATION_VALID_DIR:str="validated"
DATA_VALIDATION_INVALID_DIR:str="invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str="drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str="report.yaml"

'''Data Transformation related constants start with DATA_TRANSFORMATION_VAR_NAME'''
##knn imputer to replace nan values
DATA_TRANSFORMATION_DIR_NAME:str="data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str="transformed"
DATA_TRANSFORMATION_OBJECT_DIR:str="transformed_object"
DATA_TRANSFORMATION_PREPROCESSING_OBJECT_FILE_NAME:str="preprocessor.pkl"

DATA_TRANSFORMATION_IMPUTER_PARAMS:dict={
    "missing_values":np.nan,
    "n_neighbors":3,
    "weights":"uniform",
}

'''Model Trainer related constants start with MODE TRAINER VAR NAME'''
MODEL_TRAINER_DIR_NAME:str="model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR:str="trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME:str="model.pkl"
MODEL_TRAINER_EXPECTED_SCORE:str=0.6
MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD:str=0.05
