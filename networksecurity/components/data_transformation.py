from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    TrainingPipelineConfig
)

import sys


if __name__ == '__main__':
    try:

        # ================= TRAINING PIPELINE CONFIG =================
        trainingpipelineconfig = TrainingPipelineConfig()

        # ================= DATA INGESTION =================
        dataingestionconfig = DataIngestionConfig(
            trainingpipelineconfig
        )

        data_ingestion = DataIngestion(
            dataingestionconfig
        )

        logging.info("Initiating Data Ingestion")

        dataingestionartifact = (
            data_ingestion.initiate_data_ingestion()
        )

        logging.info("Data Ingestion Completed")

        print(dataingestionartifact)

        # ================= DATA VALIDATION =================
        data_validation_config = DataValidationConfig(
            trainingpipelineconfig
        )

        data_validation = DataValidation(
            dataingestionartifact,
            data_validation_config
        )

        logging.info("Initiating Data Validation")

        data_validation_artifact = (
            data_validation.initiate_data_validation()
        )

        logging.info("Data Validation Completed")

        print(data_validation_artifact)

        # ================= DATA TRANSFORMATION =================
        data_transformation_config = DataTransformationConfig(
            trainingpipelineconfig
        )

        data_transformation = DataTransformation(
            data_validation_artifact,
            data_transformation_config
        )

        logging.info("Initiating Data Transformation")

        data_transformation_artifact = (
            data_transformation.initiate_data_transformation()
        )

        logging.info("Data Transformation Completed")

        print(data_transformation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)