import json
import os

from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaConsumer

from app.dbs.mongodb.repository.row_data_repository import insert_email

load_dotenv(verbose=True)


def consume_row_data():
    data = KafkaConsumer(
        os.environ['TOPIC_ROW_DATA'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    print('listing...')
    for message in data:
        insert_email(message.value)
        print(f'received: {message.key} : {message.value}')


app = Flask(__name__)
if __name__ == '__main__':
    consume_row_data()
