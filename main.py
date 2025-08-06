from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys
import os
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
if __name__ == "__main__":
    try:
        trainingPipelineConfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingPipelineConfig)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("Data Ingestion started")
        dataingestionartifact = dataingestion.initiate_data_ingestion
        print(dataingestionartifact)
        logging.info("Data Ingestion completed")
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e