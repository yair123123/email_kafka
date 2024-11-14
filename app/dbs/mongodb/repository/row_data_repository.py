from typing import Dict

from app.dbs.mongodb.database.config import row_data_collection


def insert_email(email:Dict[str,str]):
    row_data_collection.insert_one(email)