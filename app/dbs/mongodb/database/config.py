import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(verbose=True)
client = MongoClient(os.environ['DB_URL'])
taxi_db = client[os.environ['DB']]


row_data_collection = taxi_db['row_data']
