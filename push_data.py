import os
import sys
import json
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(f"MongoDB URL: {MONGO_DB_URL}")

import certifi
ca=certifi.where()

import pandas as pd
import pymongo
import numpy as np
from networksecurity.logging.logger import logger
from networksecurity.exception.exception import NetworkSecurityException


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def cv_to_json_convertor(self, file_path):

        try:
            data = pd.read_csv(file_path)
            # Convert dataframe to list of dicts
            records = data.to_dict(orient='records')
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
            logger.info("CSV to JSON conversion successful")
    
    def insert_data_to_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongo_client =pymongo.MongoClient(MONGO_DB_URL)  
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]  
            self.collection.insert_many(self.records)
            logger.info("Data inserted successfully into MongoDB")
            return(len(self.records))          
            
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == '__main__':
    FILE_PATH = FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE="network_security"
    COLLECTION="NetworkData"
    networkobj=NetworkDataExtract()
    records = networkobj.cv_to_json_convertor(FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_to_mongodb(records,DATABASE,COLLECTION)
    print(no_of_records)