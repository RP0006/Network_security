import os
import sys

import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from networksecurity.constants.training_pipeline import TARGET_COLUMN, DATA_TRANSFORMATION_IMPUTER_PARAMS
from networksecurity.entity.artifact_entity import DataTransformationArtifact, DataValidationArtifact
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import save_numpy_array_data, save_object


class DataTransformation:
    def __init__(
        self,
        data_validation_artifact: DataValidationArtifact,
        data_transformation_config: DataTransformationConfig,
    ):
        try:
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    @staticmethod
    def read_data(file_path: str) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def get_data_transformer_object(self) -> Pipeline:
        try:
            imputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            scaler = StandardScaler()
            preprocessing_pipeline = Pipeline(
                steps=[
                    ("imputer", imputer),
                    ("scaler", scaler),
                ]
            )
            return preprocessing_pipeline
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_transformation(self) -> DataTransformationArtifact:
        try:
            train_df = self.read_data(
                self.data_validation_artifact.valid_train_file_path
            )
            test_df = self.read_data(
                self.data_validation_artifact.valid_test_file_path
            )

            if TARGET_COLUMN not in train_df.columns:
                raise Exception(
                    f"Target column '{TARGET_COLUMN}' not found in training data"
                )
            if TARGET_COLUMN not in test_df.columns:
                raise Exception(
                    f"Target column '{TARGET_COLUMN}' not found in testing data"
                )

            input_feature_train_df = train_df.drop(columns=[TARGET_COLUMN])
            target_feature_train_df = train_df[TARGET_COLUMN]
            input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN])
            target_feature_test_df = test_df[TARGET_COLUMN]

            preprocessing_obj = self.get_data_transformer_object()
            transformed_input_train_arr = preprocessing_obj.fit_transform(
                input_feature_train_df
            )
            transformed_input_test_arr = preprocessing_obj.transform(
                input_feature_test_df
            )

            transformed_train_arr = np.c_[
                transformed_input_train_arr,
                np.array(target_feature_train_df).reshape(-1, 1),
            ]
            transformed_test_arr = np.c_[
                transformed_input_test_arr,
                np.array(target_feature_test_df).reshape(-1, 1),
            ]

            save_numpy_array_data(
                file_path=self.data_transformation_config.transformed_train_file_path,
                array=transformed_train_arr,
            )
            save_numpy_array_data(
                file_path=self.data_transformation_config.transformed_test_file_path,
                array=transformed_test_arr,
            )
            save_object(
                file_path=self.data_transformation_config.transformed_object_file_path,
                obj=preprocessing_obj,
            )

            data_transformation_artifact = DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path,
            )

            logging.info(
                f"Data Transformation Artifact: {data_transformation_artifact}"
            )
            return data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
