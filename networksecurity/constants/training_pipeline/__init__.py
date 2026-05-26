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

'''Data Ingeestion related constants start with DATA_INGESTION_VAR_NAME'''

DATA_INGESTION_COLLECTION_NAME:str="Network_Data"
DATA_INGESTION_DATABASE_NAME:str="Rohit"
DATA_INGESTION_FILE_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float=0.2